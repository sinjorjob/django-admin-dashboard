# Generated by Django 3.2.4 on 2021-06-09 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='製品名')),
                ('price', models.IntegerField(default=0, verbose_name='価格')),
            ],
            options={
                'db_table': 'm_product',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='購入日時')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.product', verbose_name='製品名')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='購入ユーザ')),
            ],
            options={
                'db_table': 't_sale',
            },
        ),
        migrations.CreateModel(
            name='SaleSummary',
            fields=[
            ],
            options={
                'verbose_name': '販売概要',
                'verbose_name_plural': '販売概要',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('dashboard.sale',),
        ),
    ]
