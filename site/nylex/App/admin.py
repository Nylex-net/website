from django.contrib import admin
from .models import Page
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import RedirectView
# from .forms import SecurityKeyAuthenticationForm

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# Override the default admin login view to use the custom form
# class CustomAdminSite(admin.AdminSite):
#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path('login/', RedirectView.as_view(url='/oidc/authenticate/')),
#         ]
#         return custom_urls + urls

admin.site.register(Page, PageAdmin)