from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Article

def new(request):
    if request.method == 'POST':
        print(request.POST)
        
        new_article = Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category'],
        )
        return redirect('list')
        
    categories = Article.CATEGORY_CHOICES  # 'CATEGORY_CHOICES'를 직접 사용하여 카테고리 목록을 전달
    return render(request, 'new.html', {'categories': categories})

def list(request):
    articles = Article.objects.all()
    categories = Article.objects.values('category').annotate(total=Count('category')).order_by('category')
    return render(request, 'list.html', {'articles': articles, 'categories': categories})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article': article})

def detail_category(request, category):
    articles = Article.objects.filter(category=category)
    total_articles = articles.count()

    return render(request, 'category.html', {'articles': articles, 'total_articles': total_articles, 'category': category})
