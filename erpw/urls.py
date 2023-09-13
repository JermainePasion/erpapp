from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='erpw-home'),
    path('users/', views.users, name='erpw-users'),
]
