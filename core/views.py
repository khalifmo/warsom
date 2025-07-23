import logging
from django.views.generic import ListView
from .models import Article  # Or whatever model you're using

logger = logging.getLogger(__name__)

class ArticleListView(ListView):
    model = Article
    template_name = "core/article_list.html"

    def get_queryset(self):
        logger.info("Fetching articles...")
        queryset = super().get_queryset()
        logger.info(f"Found {queryset.count()} articles.")
        return queryset
