"""
URL configuration for nylex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from mozilla_django_oidc.views import OIDCAuthenticationRequestView, OIDCAuthenticationCallbackView

def admin_login_redirect(request):
    return redirect('/oidc/authenticate/')

urlpatterns = [
    # path('admin/login/', OIDCAuthenticationRequestView.as_view(), name='oidc_authentication_init'),  # Override admin login 
    path('oidc/callback/', OIDCAuthenticationCallbackView.as_view, name='oidc_callback'),
    path('admin/login/', admin_login_redirect),
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('admin/', admin.site.urls),
    path('', include('App.urls')),
    # path('oidc/login/', OIDCAuthenticationRequestView.as_view(), name='oidc_authentication_init'),
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
    # urlpatterns.append(path("__debug__/", include(App.urls)))