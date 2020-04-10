from django.db import models

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category' 
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    content = models.TextField()
    summary = models.CharField(max_length=100)
    datePosted = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:100]
