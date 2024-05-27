from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Article, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from functools import wraps

# Decorator to update last viewed information
def update_last_viewed(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        if request.user.is_authenticated:
            article_id = kwargs.get('article_id')
            if article_id:
                Article.objects.filter(id=article_id).update(
                    last_viewed=timezone.now(),
                    last_viewer=request.user
                )
        return response
    return wrapper

@login_required
def new(request):
    if request.method == 'POST':
        new_article = Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category'],
            author=request.user  # 현재 로그인한 사용자
        )
        return redirect('list')
    
    categories = Article.CATEGORY_CHOICES
    return render(request, 'new.html', {'categories': categories})

def list(request):
    articles = Article.objects.all()
    categories = Article.objects.values('category').annotate(total=Count('category')).order_by('category')
    return render(request, 'list.html', {'articles': articles, 'categories': categories})

@login_required
@update_last_viewed
def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        content = request.POST.get('comment_content')
        Comment.objects.create(article=article, content=content)
        return HttpResponseRedirect(reverse('detail', args=[article_id]))
    comments = article.comments.all()
    return render(request, 'detail.html', {'article': article, 'comments': comments})

def detail_category(request, category):
    articles = Article.objects.filter(category=category)
    total_articles = articles.count()
    return render(request, 'category.html', {'articles': articles, 'total_articles': total_articles, 'category': category})

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    article_id = comment.article.id
    comment.delete()
    return HttpResponseRedirect(reverse('detail', args=[article_id]))

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'error': '로그인 실패. 다시 시도해주세요.'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('list')  # Redirect to a page of your choice
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
