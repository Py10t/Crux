from django.urls import path

from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.index, name='stock_index'),
    path('articles/', views.artikel, name='stock_articles'),
    path('materials/', views.material, name='stock_materials'),
    path('machines/', views.maschinen, name='stock_machines'),
    path('customers/', views.kunden, name='stock_customers'),
]
