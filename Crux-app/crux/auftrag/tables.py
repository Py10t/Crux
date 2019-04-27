import django_tables2 as tables
from bestellung.models import Order


class OrderTable(tables.Table):
    """this is the index table for contracts"""
    class Meta:
        model = Order
        template_name = 'django_tables2/bootstrap.html'
        exclude = ['order_status', 'id', 'collection', 'collection_name']


    my_column = tables.TemplateColumn(verbose_name=('Optionen'),
                                      template_name='auftrag/next_button.html')