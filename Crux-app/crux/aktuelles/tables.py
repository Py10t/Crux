import django_tables2 as tables
from .models import Aktuelles
from stock.models import Article, Stock
from bestellung.models import Order


class AktuellesTable(tables.Table):
    class Meta:
        # print("inside class Meta")
        model = Order
        template_name = 'django_tables2/bootstrap.html'
        # sequence = ('article', 'delivery_date', 'amount', 'order_status', 'customer')
        # exclude = ['order_date', 'id', 'collection', 'collection_name', 'order_number_ext', 'order_number_int']
        fields = ['article', 'delivery_date', 'amount', 'order_status', 'customer']


    my_column = tables.TemplateColumn(verbose_name=('Lager'),
                                      template_name='aktuelles/stock_amount.html')


