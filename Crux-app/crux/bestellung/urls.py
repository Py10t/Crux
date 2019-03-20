from django.urls import path

from . import views

urlpatterns = [
    # ex: bestellung/
    path('', views.index, name='index'),
]
