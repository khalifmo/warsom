from django.urls import path
from .views import ArticleListView, article_detail

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>/', article_detail, name='article-detail'),
]
