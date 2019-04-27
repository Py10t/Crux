from django.urls import path

from . import views

urlpatterns = [
    # AUFTRAG URLS
    path('', views.index, name='rechnung_index'),
]
