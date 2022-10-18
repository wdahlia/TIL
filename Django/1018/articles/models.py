from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='images/')
    thumbnail = ProcessedImageField(
        upload_to='images/', 
        blank=True,
        processors=[ResizeToFill(1500, 1000)], 
        format='JPEG',
        options={'quality': 80})


class Comment(models.Model):
    content = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)