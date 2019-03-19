# stock/tables.py
import django_tables2 as tables
from .models import Article, Material

class ArticleTable(tables.Table):
    class Meta:
        model = Article
        template_name = 'django_tables2/bootstrap.html'