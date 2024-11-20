# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post-list'),  # List Posts
    path('posts/create/', views.post_create, name='post-create'),  # Create Post
]
