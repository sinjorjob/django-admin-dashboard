from django.contrib import admin
from .models import Product, Sale, SaleSummary
from django.db.models import Count, Sum, Min, Max, DateTimeField
from django.db.models.functions import Trunc




class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price',)


class SaleSummaryAdmin(admin.ModelAdmin):

    change_list_template = 'admin/sale_summary_change_list.html'
    date_hierarchy = 'created'
    # --------- ここから追加 --------- 
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Count('id'),
            'total_sales': Sum('product__price'),
        }

        response.context_data['summary'] = list(
            qs
            .values('product__product_name')
            .annotate(**metrics)  
            .order_by('-total_sales')  #降順
        )
        # 合計金額の取得
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics))

       
        #日付ごとの売上合計値を計算
        # {'period': datetime.datetime(2021, 4, 1, 0, 0, tzinfo=<DstTzInfo 'Asia/Tokyo' JST+9:00:00 STD>), 'total': 5000}
        summary_over_time = qs.annotate(
            period=Trunc('created', 'day', output_field=DateTimeField()),
        ).values('period').annotate(total=Sum('product__price')).order_by('period')

        #売上の累積値を計算
        total_price = 0
        cumulative_value_of_prices = []
        for price in summary_over_time:
            total_price = total_price + price['total']
            cumulative_value_of_prices.append(total_price)
        response.context_data['cumulative_value_of_prices'] = cumulative_value_of_prices

        
        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
        } for x in summary_over_time]

        return response
        

admin.site.register(SaleSummary, SaleSummaryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)