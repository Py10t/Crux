from django.urls import path

from . import views

app_name = 'rechnung'
urlpatterns = [
    # AUFTRAG URLS
    path('', views.index, name='rechnung_index'),
    path('updated/<int:record_id>', views.update_order, name='update_rechnung'),
    path('generated/<int:record_id>', views.generate_invoice, name='generate_invoice'),
]

