from django import forms
from .models import Community
# 현재 디렉토리의 models.py에서 Community 클래스를 불러와준다.

class CommunityForm(forms.ModelForm):
  class Meta:
    model = Community
    fields = ['title', 'content']

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
    }

    labels = {
      'title': '제목',
      'content': '내용',
    }