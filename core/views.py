import logging
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Article

logger = logging.getLogger(__name__)

class ArticleListView(ListView):
    model = Article
    template_name = "core/home.html"

    def get_queryset(self):
        logger.info("Fetching articles...")
        queryset = super().get_queryset()
        logger.info(f"Found {queryset.count()} articles.")
        return queryset

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "core/article_detail.html", {"article": article})
