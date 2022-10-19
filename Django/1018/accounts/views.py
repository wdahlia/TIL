from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout
from .forms import UserCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from articles.models import Article, Comment
# Create your views here.

def login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('accounts:login')
    else:
        login_form = AuthenticationForm()
    
    context = {
        'login_form' : login_form,
    }
    
    return render(request, 'accounts/main.html', context)

def signup(request):
    if request.method == "POST":
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('accounts:login')

    else:
        signup_form = UserCreateForm()

    context = {
        'signup_form' : signup_form,
    }

    return render(request, 'accounts/signup.html', context)

@login_required
def logout(request):
    auth_logout(request)
    messages.warning(request, 'Bye!')
    return redirect('accounts:login')


@login_required
def detail(request, user_pk):
    article_list = Article.objects.filter(user_id=user_pk)
    comment_list = Comment.objects.filter(user_id=user_pk)

    context = {
        'article_list' : article_list,
        'comment_list' : comment_list,
    }

    return render(request, 'accounts/profile.html', context)