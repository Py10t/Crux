from django.shortcuts import render
from .tables import AktuellesTable
from bestellung.models import Order
from stock.models import Stock


def index(request):
    # print("index views")
    all_orders = Order.objects.all().order_by('delivery_date')
    # print(all_orders)
    # print(Order.objects.all())

    print('Start hier 1')
    for item in all_orders:
        item.stock_amount = Stock.objects.get(article=item.article.pk)
        print(type(item.stock_amount))
        # item.delivery_date = item.delivery_date.strftime("%d/%m/%Y, %H:%M:%S")
        # print(item.delivery_date)

    table = AktuellesTable(all_orders)
    print('Start hier 2')
    for item in all_orders:
        print(type(item.stock_amount))
    # table = AktuellesTable(Order.objects.all())
    # print(dir(table))
    # for item in all_orders:
    #     print(item.article.pk)
    #     print(Stock.objects.all())
    #     print(Stock.objects.get(article=item.article.pk))
    #     print(type(item.article.name))

    return render(request, "aktuelles/index.html", {
        "table": table
    })