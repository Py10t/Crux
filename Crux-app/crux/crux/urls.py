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
    path('', include('homepage.urls')),
    path('homepage/', include('homepage.urls')),
    path('textdocs/', include('textdocs.urls')),
    path('maschinenplanung/', include('maschinenplanung.urls')),
    path('bestellung/', include('bestellung.urls')),
    path('auftrag/', include('auftrag.urls')),
    path('polls/', include('polls.urls')),
    path('stock/', include('stock.urls')),
    path('admin/', admin.site.urls),
    # url(r'^login/$', login, {'template_name': 'toggle_login.html'},
    #     name='mysite_login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout',
    #     {'next_page': reverse_lazy('marcador_bookmark_list')}, name='mysite_logout'),
]
