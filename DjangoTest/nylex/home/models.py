from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    header = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='media')
    content = RichTextField()
    pub_date = models.DateTimeField('date published')

def __str__(self):
        return self.title
    # def get_absolute_url(self, *args, **kwargs):
    #     slug = slugify(self.alias)
    #     return reverse("article", kwargs={"pk": self.id, "slug": self.slug})
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)