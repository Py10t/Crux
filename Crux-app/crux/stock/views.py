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
