# Generated by Django 2.2.7 on 2019-11-07 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bestellung', '0012_auto_20191107_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stock.Customer', verbose_name='Kunde'),
        ),
    ]
