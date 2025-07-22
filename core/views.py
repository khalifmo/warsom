from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = "core/home.html"  # Make sure this template exists
    context_object_name = "articles"
    paginate_by = 10
    ordering = ["-published_at"]

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "core/article_detail.html", {"article": article})
