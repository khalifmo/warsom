
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="home"),
    path("article/<int:pk>/", views.article_detail, name="article_detail"),
]


