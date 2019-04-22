# stock/tables.py
import django_tables2 as tables
from .models import Material, Article, MouldingMachine, Customer, Tooling


class MaterialTable(tables.Table):
    class Meta:
        model = Material
        template_name = 'django_tables2/bootstrap.html'


class ArticleTable(tables.Table):
    class Meta:
        model = Article
        template_name = 'django_tables2/bootstrap.html'


class MouldingMachineTable(tables.Table):
    class Meta:
        model = MouldingMachine
        template_name = 'django_tables2/bootstrap.html'


class CustomerTable(tables.Table):
    class Meta:
        model = Customer
        template_name = 'django_tables2/bootstrap.html'


class ToolingTable(tables.Table):
    class Meta:
        model = Tooling
        template_name = 'django_tables2/bootstrap.html'
