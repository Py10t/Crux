from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generated/<int:record_id>', views.generate_stock_amount, name='generate_stock_amount'),
]