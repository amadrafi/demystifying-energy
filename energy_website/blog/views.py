from django.http import HttpResponse
from .models import Article, Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
# Create your views here.

def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'articles':articles})

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

def article_detail(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    comments = articles.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.articles = articles
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/article_template.html', {'articles':articles, 'comments': comments,
                                                            'new_comment': new_comment,
                                                            'comment_form': comment_form})
