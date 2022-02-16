from django.urls import path
from .views import BlogListViuw, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', BlogListViuw.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('post/new/', PostCreateView.as_view(), name='new_post'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
]
