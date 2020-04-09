from django.db import models

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
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
