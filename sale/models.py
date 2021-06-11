from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=100,verbose_name ="製品名")
    price = models.IntegerField(default=0,verbose_name ="価格") 

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'm_product'


class Sale(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.PROTECT,verbose_name ="購入ユーザ")
    product = models.ForeignKey(Product, on_delete = models.PROTECT,verbose_name ="製品名")
    created = models.DateTimeField("購入日時")

    class Meta:
        db_table = 't_sale'


class SaleSummary(Sale):
    class Meta:
        proxy = True
        verbose_name = '販売概要'
        verbose_name_plural = '販売概要'

