from django.shortcuts import render
from django.template import loader
from stock.models import Article
# Create your views here.


def index(request):
    """renders index view, needs args for rectangle sizes"""
    day_week_month = [1, 2, 3, 4, 5, 6, 7]
    return render(request, 'maschinenplanung/index.html', {'articles': Article.objects.all()})