from django.urls import path
from . import views
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap

from blog.sitemaps import(
    StaticViewSitemap,
    ArticleSitemap,
    CategorySitemap
)

sitemaps = {
    "static": StaticViewSitemap,
    "article": ArticleSitemap,
    "category": CategorySitemap
}

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('sitemap.xml/', sitemap, {"sitemaps" : sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path(
        "robots.txt/",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    url(r'^article/(?P<slug>[\w-]+)/$', views.article_detail, name='link'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.list_by_category, name='list_by_category'),
    
]
