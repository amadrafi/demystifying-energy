from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    datePosted = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:100]
