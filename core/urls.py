from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = "core/article_list.html"  # Adjust if your template path differs
    context_object_name = "articles"
    paginate_by = 10  # Optional: paginate 10 articles per page
    ordering = ["-published_at"]  # Show newest articles first

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "core/article_detail.html", {"article": article})
