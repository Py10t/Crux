# Generated by Django 2.2.7 on 2019-11-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestellung', '0008_order_stock_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(default='07/11/2019, 11:43:09', verbose_name='Lieferdatum'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default='07/11/2019, 11:43:09', verbose_name='Bestelldatum'),
        ),
        migrations.AlterField(
            model_name='order',
            name='stock_amount',
            field=models.BigIntegerField(default=0, verbose_name='Lagermenge'),
        ),
    ]
