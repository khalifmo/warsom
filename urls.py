from django.contrib import admin
from django.urls import path
from core.views import ArticleListView, article_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticleListView.as_view(), name='home'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
]
