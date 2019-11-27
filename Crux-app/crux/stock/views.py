from django.shortcuts import render
from django.http import HttpResponse
from .models import Material, Article, MouldingMachine, Customer, Tooling
from .tables import ArticleTable, MaterialTable, MouldingMachineTable, CustomerTable, ToolingTable
# Create your views here.


# def detail(request, article_id):
#     return HttpResponse("<h2>Details for Article id: " + str(article_id) + "</h2")

def index(request):
    article = ArticleTable(Article.objects.all())
    material = MaterialTable(Material.objects.all())
    moulding_machine = MouldingMachineTable(MouldingMachine.objects.all())
    customer = CustomerTable(Customer.objects.all())
    tooling = ToolingTable(Tooling.objects.all())

    context = {
        'article': article,
        'material': material,
        'moulding_machine': moulding_machine,
        'customer': customer,
        'tooling': tooling,
    }
    return render(request, 'stock/index.html', context)

def artikel(request):
    article = ArticleTable(Article.objects.all())
    print("immer hier")

    context = {
        'article': article,
    }
    return render(request, 'stock/artikel.html', context)

def material(request):
    material = MaterialTable(Material.objects.all())

    context = {
        'material': material,
    }
    return render(request, 'stock/material.html', context)

def maschinen(request):
    moulding_machine = MouldingMachineTable(MouldingMachine.objects.all())

    context = {
        'moulding_machine': moulding_machine,
    }
    return render(request, 'stock/maschinen.html', context)

def kunden(request):

    customer = CustomerTable(Customer.objects.all())

    context = {
        'customer': customer,
    }
    return render(request, 'stock/kunden.html', context)
