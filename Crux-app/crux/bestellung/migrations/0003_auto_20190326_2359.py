# Generated by Django 2.1.4 on 2019-03-26 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestellung', '0002_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.BigIntegerField(verbose_name='Menge'),
        ),
        migrations.AlterField(
            model_name='order',
            name='company',
            field=models.CharField(max_length=250, verbose_name='Firma'),
        ),
    ]
