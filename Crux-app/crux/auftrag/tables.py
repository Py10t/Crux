# stock/tables.py
import django_tables2 as tables
from django_tables2 import TemplateColumn
from bestellung.models import Order

class OrderTable(tables.Table):
    class Meta:
        model = Order
        template_name = 'django_tables2/bootstrap.html'


    my_column = tables.TemplateColumn(verbose_name=('Optionen'),
                                      template_name='auftrag/next_button.html')