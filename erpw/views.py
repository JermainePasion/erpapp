from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def home (request):
    return render (request, 'erpw/home.html')

def users (request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'erpw/users.html', context)

