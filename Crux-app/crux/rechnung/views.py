from django.shortcuts import render
from django_tables2 import RequestConfig
from bestellung.models import Order
from .tables import OrderTable
from django.shortcuts import redirect

# Create your views here.

def index(request):
    """index view is a table showing all orders"""
    table_single = OrderTable(Order.objects.filter(order_status="Rechnung", collection=False))
    table_collection = OrderTable(Order.objects.filter(order_status="Rechnung", collection=True))
    RequestConfig(request).configure(table_single)
    context = {
        'table_single': table_single,
        'table_collection': table_collection,
    }
    return render(request, 'rechnung/index.html', context)

def update_order(request, record_id):
    """update_order pushes via order_status from order up to invoice"""
    obj = Order.objects.get(pk=record_id)
    obj.order_status = 'Done'
    obj.save()
    print('item updated: ' + str(record_id))
    response = redirect('/rechnung/')
    return response

def generate_invoice(request, record_id):
    """generates invoice via pk """
    rechnung = Order.objects.get(pk=record_id)
    customer = rechnung.customer
    #customer is a foreignkey
    preis = rechnung.article.price_per_piece*rechnung.amount
    print(rechnung.article.price_per_piece)
    # print(customer.city)
    context = {
        'rechnung': rechnung,
        'customer': customer,
        'preis': preis,
    }
    return render(request, 'textdocs/invoice.html', context)
