from django.contrib import admin
from django.urls import path, include
from .views import invoice, render_invoice

urlpatterns = [
    path("", invoice, name='invoice'),
    path("render/<int:pk>", render_invoice, name='invoice-render'),
    # path("send/<int:pk>", send_email, name='invoice-send'),

]