from django.urls import path

from . import views

app_name = 'stock'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='stock_index'),
    # path('article/', views.article, name='article'),
    # path('new_table/', views.create_table, name='add_table')
]
