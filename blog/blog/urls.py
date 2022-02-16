from django.urls import path
from .views import BlogListViuw, PostDetailView

urlpatterns = [
    path('', BlogListViuw.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
]
