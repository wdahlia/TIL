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
   