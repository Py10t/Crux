from django.shortcuts import render
from django.http import HttpResponse
from django_tables2 import RequestConfig
from .models import Article, Material
from django.template import loader
from .tables import ArticleTable
# Create your views here.


def detail(request, article_id):
    return HttpResponse("<h2>Details for Article id: " + str(article_id) + "</h2")

def index(request):
    return render(request, 'stock/index.html', {'articles': Article.objects.all()})

def article(request):
    table = ArticleTable(Article.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'stock/article.html', {'table': table})