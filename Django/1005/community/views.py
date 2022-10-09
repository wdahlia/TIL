from django.shortcuts import render, redirect
from .forms import CommunityForm
from .models import  Community

# Create your views here.


def index(request):
    community = Community.objects.all()
    
    context = {
        'community' : community
    }
    return render(request, 'communities/index.html', context)

def create(request):
    if request.method == 'POST':
        create_article = CommunityForm(request.POST)
        if create_article.is_valid():
            create_article.save()
            return redirect('community:index')
    else:
        create_article = CommunityForm()
    context = {
        'create_article' : create_article,
    }

    return render(request, 'communities/new.html', context)

def delete(request, id):
    Community.objects.get(pk=id).delete()
    return redirect('community:index')

def update(request, pk):
    community = Community.objects.get(pk=pk)

    if request.method == "POST":
        edit_article = CommunityForm(request.POST, instance=community)
        if edit_article.is_valid():
            edit_article.save()
            return redirect('community:index')
    else:
        edit_article = CommunityForm(instance=community)
    context = {
        'edit_article' : edit_article,
    }

    return render(request, 'communities/edit.html', context)