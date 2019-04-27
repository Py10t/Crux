from django.shortcuts import render
from django_tables2 import RequestConfig
from bestellung.models import Order
from .tables import OrderTable
from django.shortcuts import redirect

# Create your views here.

def index(request):
    """index view is a table showing all orders"""
    table_single = OrderTable(Order.objects.filter(order_status="Lieferschein", collection=False))
    table_collection = OrderTable(Order.objects.filter(order_status="Lieferschein", collection=True))
    RequestConfig(request).configure(table_single)
    context = {
        'table_single': table_single,
        'table_collection': table_collection,
    }
    return render(request, 'lieferschein/index.html', context)

def update_order(request, record_id):
    """update orders order_status überführt von einer Stufe zur nächsten"""
    obj = Order.objects.get(pk=record_id)
    obj.order_status = 'Rechnung'
    obj.save()
    print('item updated: ' + str(record_id))
    response = redirect('/lieferschein/')
    return response
