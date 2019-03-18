from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Material
from django.template import loader
# Create your views here.

"""def index(request):
    all_articles = Article.objects.all()
    html = ''
    for article in all_articles:
        url = '/stock/' + str(article.id) + '/'
        html += '<a href="' + url + '">' + article.name + '</a><br>'
    return HttpResponse(html)"""

def detail(request, article_id):
    return HttpResponse("<h2>Details for Article id: " + str(article_id) + "</h2")

def index(request):
    return render(request, 'stock/index.html', {'articles': Article.objects.all()})