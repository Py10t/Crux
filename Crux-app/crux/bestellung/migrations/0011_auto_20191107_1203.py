# Generated by Django 2.2.7 on 2019-11-07 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bestellung', '0010_auto_20191107_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Article', verbose_name='Artikel'),
        ),
    ]