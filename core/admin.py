
from django.contrib import admin
from .models import Article, Source

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at")
    list_filter = ("published_at", "sources")
    search_fields = ("title", "summary")

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ("name", "bias")
    search_fields = ("name",)


