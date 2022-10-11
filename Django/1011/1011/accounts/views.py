from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import UserForm
# Create your views here.

def main(request):
    return render(request, 'accounts/main.html')

def index(request):
    user_list = get_user_model().objects.order_by('-id')

    context = {
        'user_list' : user_list,
    }

    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method == "POST":
        signup_list = UserForm(request.POST)
        if signup_list.is_valid():
            signup_list.save()
            return redirect('account:index')

    else:
        signup_list = UserForm()
    
    context = {
        'signup_list' : signup_list,
    }

    return render(request, 'accounts/signup.html', context)

def detail(request, user_pk):
    user_detail = get_user_model().objects.get(pk=user_pk)

    context = {
        'user_detail' : user_detail,
    }

    return render(request, 'accounts/detail.html', context)