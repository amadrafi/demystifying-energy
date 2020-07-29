from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Article, Category


class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return['blog:blog-about', 'blog:blog-home']

    def location(self, item):
        return reverse(item)

class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Article.objects.filter(status=1)

class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = '0.4'

    def items(self):
        return Category.objects.all()