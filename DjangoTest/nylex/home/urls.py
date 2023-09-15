from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # path originally '/home' instead of ''.
    path('home', views.home, name='home'),
    path('search', views.search, name='search'),
    path('site-map', views.site_map, name='site-map'),
    path('<slug:slug>', views.template, name='article')
]