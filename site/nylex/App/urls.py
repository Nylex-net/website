from django.urls import path, include
from App.views import page_view_set
from rest_framework import routers
import django.conf.urls
from App.views import custom404, custom500, register_security_key, authenticate_with_security_key
from .forms import SecurityKeyAuthenticationForm

# define the router
router = routers.DefaultRouter()
router.register(r'page', page_view_set) #the route tha will be used to access your API on the browser

urlpatterns = [
    path('', page_view_set.home, name='home'), # path originally '/home' instead of ''.
    path('home/', page_view_set.home, name='home'),
    path('search/', page_view_set.search, name='search'),
    path('site-map/', page_view_set.site_map, name='site-map'),
    path('<slug:slug>/', page_view_set.template, name='<slug:slug>'),
    path('api-auth/', include('rest_framework.urls')),
    path('register-security-key/', register_security_key, name='register_security_key'),
    path('login-security-key/', authenticate_with_security_key, name='login_security_key'),
    path('admin/login/', authenticate_with_security_key.as_view(authentication_form=SecurityKeyAuthenticationForm))
]

django.conf.urls.handler404 = custom404
django.conf.urls.handler500 = custom500