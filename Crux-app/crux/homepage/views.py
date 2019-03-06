from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import datetime


# Create your views here.

def index(request):
    dt = datetime.datetime.now()
    aktuelle_kw = dt.isocalendar()[1]
    aktuelle_kw_string = "KW " + str(aktuelle_kw)

    template = loader.get_template('homepage/index.html')
    context = {
        'aktuelle_kw_string': aktuelle_kw_string
    }

    return HttpResponse(template.render(context, request))


from django.shortcuts import render

# Create your views here.
