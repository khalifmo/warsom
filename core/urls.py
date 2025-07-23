from django.urls import path
from .views import home

urlpatterns = [
    path('', home),  # This is the home page
]
