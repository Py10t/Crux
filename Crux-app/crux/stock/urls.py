from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('article/', views.article, name='article'),
    # path('new_table/', views.create_table, name='add_table')
]