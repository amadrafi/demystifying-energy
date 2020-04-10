from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.

def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'articles':articles})

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

def article_detail(request, slug):
    articles = Article.objects.get(slug=slug)
    return render(request, 'blog/article_template.html', {'articles':articles})
