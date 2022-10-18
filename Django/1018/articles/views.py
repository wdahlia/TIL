from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.

@login_required
def index(request):
    card_list = Article.objects.all()
    
    context = {
        'card_list' : card_list,
    }

    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        create_form = ArticleForm(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, '글 작성 완료!')
            return redirect('articles:index')
    else:
        create_form = ArticleForm()
    
    context = {
        'create_form' : create_form,
    }
        
    return render(request, 'articles/create.html', context)

@login_required
def detail(request, pk):
    article_detail = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article_detail.comment_set.all()
    context = {
        'article_detail' : article_detail,
        'comment_form' : comment_form,
        'comments' : comments,
    }

    return render(request, 'articles/detail.html', context)

@login_required
def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    
    return redirect('articles:index')

@login_required
def update(request, pk):
    article_update = Article.objects.get(pk=pk)
    if request.method == "POST":
        update_form = ArticleForm(request.POST, request.FILES, instance=article_update)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, '수정 완료!')
            return redirect('articles:index')
    else:
        update_form = ArticleForm(instance=article_update)

    context = {
        'update_form' : update_form,
    }

    return render(request, 'articles/edit.html', context)

@login_required
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()

    return redirect('articles:detail', article.pk)


@login_required
def comments_delete(request, article_pk, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()
    return redirect('articles:detail', article_pk)