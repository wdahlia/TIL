from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = 'Article'
        fields = ['title', 'content', 'movie_name']

        labels = {
            'title' : '리뷰 제목',
            'content' : '리뷰 내용',
            'movie_name' : '영화제목',            
        }
