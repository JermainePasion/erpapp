from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def home (request):
    return render (request, 'inventory/dashboard.html')

@login_required
def users (request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'erpw/users.html', context)

