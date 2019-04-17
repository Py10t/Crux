from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_tables2 import RequestConfig
from .models import Article, Material
from django.template import loader
from .tables import ArticleTable
# from .forms import TableForm
# Create your views here.


def detail(request, article_id):
    return HttpResponse("<h2>Details for Article id: " + str(article_id) + "</h2")

def index(request):
    return render(request, 'stock/index.html', {'articles': Article.objects.all()})

def article(request):
    table = ArticleTable(Article.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'stock/article.html', {'table': table})

# def create_table(request):
#     form = TableForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         table = form.save(commit=False)
#         # order.save()
#         response = redirect('/bestellung/')
#         return response
#
#     context = {
#         "form": form,
#     }
#     return render(request, 'bestellung/order_form.html', context)