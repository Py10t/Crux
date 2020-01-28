"""crux URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url,include


urlpatterns = [
    path('', include('homepage.urls', namespace='homepage')),
    # path('homepage/', include('homepage.urls', namespace='homepage')),
    path('textdocs/', include('textdocs.urls')),
    path('maschinenplanung/', include('maschinenplanung.urls', namespace='maschinenplanung')),
    path('bestellung/', include('bestellung.urls', namespace='bestellung')),
    path('auftrag/', include('auftrag.urls', namespace='auftrag')),
    path('produktionsauftrag/', include('produktionsauftrag.urls', namespace='produktionsauftrag')),
    path('lieferschein/', include('lieferschein.urls', namespace='lieferschein')),
    path('rechnung/', include('rechnung.urls', namespace='rechnung')),
    path('aktuelles/', include('aktuelles.urls')),
    path('stock/', include('stock.urls', namespace='stock')),
    path('admin/', admin.site.urls),
]
