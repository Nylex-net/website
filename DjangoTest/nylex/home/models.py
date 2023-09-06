from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200)
    header = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')