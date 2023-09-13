from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Jermaine Pasion',
        'title': 'Post 1',
        'content': 'Very First Post',
        'date_posted': 'September 12, 2023',
    },
    {
        'author': 'John John',
        'title': 'Post 2',
        'content': 'Another Post',
        'date_posted': 'September 13, 2069',
    }
]
def home (request):
    return render (request, 'erpw/home.html')

def users (request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'erpw/users.html', context)

