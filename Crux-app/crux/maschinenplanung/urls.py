from django.urls import path

from . import views

app_name = 'maschinenplanung'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='maschinenplanung_index'),
]