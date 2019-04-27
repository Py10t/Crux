from django.urls import path

from . import views

urlpatterns = [
    # AUFTRAG URLS
    path('', views.index, name='lieferschein_index'),
    path('updated/<int:record_id>', views.update_order, name='update_lieferschein'),
]
