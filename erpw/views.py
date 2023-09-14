from django.shortcuts import render
from .models import Post


def home (request):
    return render (request, 'erpw/home.html')

def users (request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'erpw/users.html', context)

