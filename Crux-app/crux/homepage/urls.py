from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('login_user/', views.login_user, name='login_user'),
]