from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleEditView, ArticleDeleteView, ArticleCreateView

urlpatterns = [
    path("blog/", ArticleListView.as_view(), name='blog'),
    path("", ArticleListView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('article/<int:pk>/edit/', ArticleEditView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/new/', ArticleCreateView.as_view(), name='article_create'),
]