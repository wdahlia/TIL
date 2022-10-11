from django.db import models

# # Create your models here.

class Article(models.Model):
    movie_name = models.CharField(max_length=25)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
