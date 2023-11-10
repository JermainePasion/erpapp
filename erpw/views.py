from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin


@login_required
def home (request):
    return render (request, 'inventory/dashboard.html')

@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    template_name = 'erpw/users.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

@method_decorator(login_required, name='dispatch')
class UserPostListView(ListView):
    model = Post
    template_name = 'erpw/user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@method_decorator(login_required, name='dispatch')
class PostDeleteView(UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/users'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@method_decorator(login_required, name='dispatch')
class AddCommentView(CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.Post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = '/users'


@login_required
def users (request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'erpw/users.html', context)



