# stock/tables.py
import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import Order

# this is the index table for single orders
class OrderTable(tables.Table):
    class Meta:
        model = Order
        template_name = 'django_tables2/bootstrap.html'
        exclude = ['order_status', 'id', 'collection', 'collection_name']


    my_column = tables.TemplateColumn(verbose_name=('Optionen'),
                                      template_name='bestellung/next_button.html')


#this is the collective_order_table when you create it
class CollectiveOrderTable(tables.Table):
    class Meta:
        model = Order
        template_name = 'djang_tables2%bootstrap.html'
        exclude = ['order_status']

    my_column = tables.TemplateColumn(verbose_name=('Optionen'),
                                      template_name='bestellung/next_button.html')