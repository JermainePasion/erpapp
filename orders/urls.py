from django.contrib import admin
from django.urls import path, include
from .views import orders_list, add, show, authenticate
urlpatterns = [
    path("", orders_list, name='orders'),
    path("add/", add, name='add'),
    path("show/", show, name='show'),
    path('approve/<int:id>', authenticate, name='approve'),
]