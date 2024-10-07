from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from webauthn.models import WebAuthnUser

# Create your models here.
class Page(models.Model):

    HEADER_DROPDOWN_CHOICES = [
        ('none', 'None'),
        ('about', 'About'),
        ('services', 'Services'),
        ('more', 'More')
        # Add more dropdown options as needed
    ]

    FOOTER_SECTION_CHOICES = [
        ('none', 'None'),
        ('company', 'Nylex.net'),
        ('resources', 'Resources'),
        ('other', 'Other')
        # Add more footer section options as needed
    ]

    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200, unique=True)
    header = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='media')
    content = RichTextField()

    show_in_header = models.BooleanField(default=False)
    header_dropdown = models.CharField(max_length=50, choices=HEADER_DROPDOWN_CHOICES, default='none')

    show_in_footer = models.BooleanField(default=False)
    footer_section = models.CharField(max_length=50, choices=FOOTER_SECTION_CHOICES, default='none')
    
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
    
class UserWebAuthnCredential(WebAuthnUser):
    WebAuthnUser.user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='webauthn_credentials')