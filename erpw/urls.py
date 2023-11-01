from django.urls import path
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView
)

urlpatterns = [
    path('', views.home, name='erpw-dashboard'),
    path('users/', PostListView.as_view(), name='erpw-users'),
    path('users/<int:pk>', PostDetailView.as_view(), name='erpw-detail'),
    path('users/new/', PostCreateView.as_view(), name='erpw-create'),
    path('users/<int:pk>/update/', PostUpdateView.as_view(), name='erpw-update'),
    path('users/<int:pk>/delete/', PostDeleteView.as_view(), name='erpw-delete'),
]
