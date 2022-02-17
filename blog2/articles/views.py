from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Article


# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'blog.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'


class ArticleEditView(UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo',)
    template_name = 'article_edit.html'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('blog')


class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ('title', 'summary', 'body', 'photo', 'author',)
