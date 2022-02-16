from .views import HomePageView, AboutPageView, ContactsPageView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('contacts/', ContactsPageView.as_view(), name="contacts"),
]
