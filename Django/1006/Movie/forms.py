from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


        labels = {
            'title' : '영화 제목',
            'summary' : '영화 내용',
            'running_time' : '상영 시간',
        }