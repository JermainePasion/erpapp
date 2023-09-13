from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return HttpResponse('<h1>Home page</h1>')

def users (request):
    return HttpResponse('<h1>Users Page</h1>')

