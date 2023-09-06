from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200)
    header = models.CharField(max_length=200)
    banner = models.ImageField()
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    # def get_absolute_url(self, *args, **kwargs):
    #     slug = slugify(self.alias)
    #     return reverse("article", kwargs={"pk": self.id, "slug": self.slug})
    
    # def save(self, *args, **kwargs):
    #     value = self.title
    #     self.slug = slugify(value, allow_unicode=True)
    #     super().save(*args, **kwargs)