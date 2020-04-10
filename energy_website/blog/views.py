from django.shortcuts import render
from .models import Article
# Create your views here.

posts = [
    {
        'author': 'Irfan',
        'title': 'Blog post 1',
        'content': 'Post Content',
        'date_posted': 'April 7, 2020'
    },
    {
        'author': 'Cheryl',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 8, 2020'
    }
]
def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'articles':articles})

# def home(request):
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
