from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='link'),
]
