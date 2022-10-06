from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.

def index(request):

    reviews = Movie.objects.all()
    context = { 
        'reviews': reviews,
    }

    return render(request, 'movies/index.html', context)

def create(request):
    # 영화 작성 페이지

    if request.method == "POST":
        create_review = MovieForm(request.POST)
        if create_review.is_valid():
            create_review.save()
            return redirect("movie:index")
    else:
        create_review = MovieForm()
    
    context = {
        "create_review" : create_review,
    }

    return render(request, 'movies/create.html', context)


def delete(request, pk):
    Movie.objects.get(pk=pk).delete()

    return redirect('movie:index')


def detail(request, pk):
   detail_movie = Movie.objects.get(pk=pk)

   context = {
    "detail_movie" : detail_movie,
   }

   return render(request, 'movies/detail.html', context)
   

def edit(request, pk):
    edit_movie = Movie.objects.get(pk=pk)

    if request.method == "POST":
        edit_mv = MovieForm(request.POST, instance=edit_movie)
        if edit_mv.is_valid():
            edit_mv.save()
            return redirect('movie:index')
        
    else:
        edit_mv = MovieForm(instance=edit_movie)
    context = {
        "edit_movie" : edit_movie,
        "edit_mv" : edit_mv,
    }

    return render(request, 'movies/edit.html', context)