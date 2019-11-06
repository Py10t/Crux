from django.shortcuts import render
from .models import Aktuelles
from .tables import AktuellesTable
from bestellung.models import Order
from stock.models import Stock


def index(request):
    # print("index views")
    table = AktuellesTable(Order.objects.all())

    return render(request, "aktuelles/index.html", {
        "table": table
    })

def generate_stock_amount(request, record_id):
    """generates invoice via pk """
    # lagermenge = Stock.objects.get(pk=record_id)
    try:
        lagermenge = Stock.objects.get(name=record_id)
    except Stock.DoesNotExist:
        lagermenge = None
    print("Das ist die Lagermenge: " + str(lagermenge))
    # # print(customer.city)
    # context = {
    #     'rechnung': rechnung,
    #     'customer': customer,
    #     'preis': preis,
    # }
    return render(request, 'aktuelles/stock_amount', lagermenge)