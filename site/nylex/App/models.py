from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200, unique=True)
    header = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='media')
    content = RichTextField()

    def __str__(self):
        return self.title