from django.shortcuts import render, redirect
from .models import Article

# # Create your views here.

def index(request):
    return render(request, 'articles/index.html')
