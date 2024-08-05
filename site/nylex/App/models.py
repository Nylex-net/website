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
    
    def save(self, *args, **kwargs):
        # If the instance already has an image, delete the old image
        if self.pk:
            old_instance = Page.objects.get(pk=self.pk)
            if old_instance.banner and old_instance.banner != self.banner:
                old_instance.banner.delete(save=False)
        super(Page, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the image file when the instance is deleted
        if self.banner:
            self.banner.delete(save=False)
        super(Page, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title