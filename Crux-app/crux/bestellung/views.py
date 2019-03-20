from django.shortcuts import render
from django_tables2 import RequestConfig
from django.template import loader
from .models import Order
from .tables import OrderTable

import datetime

# Create your views here.

def index(request):

    table = OrderTable(Order.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'bestellung/index.html', {'table': table})