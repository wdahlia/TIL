from django import forms
from .models import Article, Comment
from django.forms import TextInput

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'thumbnail']

        labels = {
            'title' : '제목',
            'content' : '내용',
            'image' : '이미지',
            'thumbnail' : '썸네일',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
        labels = {
            "content" : "",
        }
        widgets = {
            'content' : TextInput(attrs={
                'class' : 'border-0 border-bottom border-1 border-dark rounded-0',
                'style' : 'background: transparent;',
                'placeholder' : '댓글을 입력해주세요'
            }),
        }
        

        