from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Order
from .tables import OrderTable


# gets table data and displays it
def index(request):

    table = OrderTable(Order.objects.filter(order_status="Bestellung"))
    RequestConfig(request).configure(table)
    return render(request, 'bestellung/index.html', {'table': table})

# gets record_id from the table to update corresponding object/obj.order_status and take it to the next lvl
# afterwards page refresh
def update_order(request, record_id):

    obj = Order.objects.get(pk=record_id)
    obj.order_status = 'Auftrag'
    obj.save()
    print('item updated: ' + str(record_id))
    table = OrderTable(Order.objects.filter(order_status="Bestellung"))
    RequestConfig(request).configure(table)
    return render(request, 'bestellung/index.html', {'table': table})