# Generated by Django 2.1.4 on 2019-04-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_auto_20190423_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='nocity', max_length=50, verbose_name='Stadt'),
        ),
        migrations.AddField(
            model_name='customer',
            name='street',
            field=models.CharField(default='nostreet', max_length=50, verbose_name='Straße'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='noname', max_length=50, verbose_name='Kunde'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='nophone', max_length=50, verbose_name='Telefon'),
        ),
    ]
