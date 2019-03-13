from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from stock.models import Article
# Create your views here.


def index(request):
    day_week_month = [1, 2, 3, 4, 5, 6, 7]
    template = loader.get_template('maschinenplanung/index.html')
    context = {'day_week_month': day_week_month}

    return HttpResponse(template.render(context, request))