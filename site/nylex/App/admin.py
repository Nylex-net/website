from django.contrib import admin
from .models import Page
from django.contrib.auth import views as auth_views
from .forms import SecurityKeyAuthenticationForm

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Page, PageAdmin)
# Override the default admin login view to use the custom form
admin.site.login_form = SecurityKeyAuthenticationForm