
from django.db import models
from django.urls import reverse

class Source(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    bias = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    summary = models.TextField()
    ai_rewrite = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True, db_index=True)
    sources = models.ManyToManyField(Source)
    media_file = models.FileField(upload_to=\'media/\', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(\'article_detail\', args=[str(self.pk)])

