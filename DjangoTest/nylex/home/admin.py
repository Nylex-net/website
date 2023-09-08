from typing import Any
from django.contrib import admin
from .models import Page
from django.utils.text import slugify
from ckeditor.widgets import CKEditorWidget
# from nylex.home import models

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # def save_model(self, request, obj, form, change):
    #     obj.slug = slugify(obj.title)
    #     super().save_model(request, obj, form, change)

admin.site.register(Page, PageAdmin)