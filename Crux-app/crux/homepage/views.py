from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import datetime


# Create your views here.

def index(request):
    dt = datetime.datetime.now()
    aktuelle_kw = dt.isocalendar()[1]
    aktuelle_kw_string = "KW " + str(aktuelle_kw)

    return render(request, 'homepage/index.html', {'aktuelle_kw_string': aktuelle_kw_string})
