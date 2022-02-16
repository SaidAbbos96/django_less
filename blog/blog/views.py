from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# Create your views here.
class BlogListViuw(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')