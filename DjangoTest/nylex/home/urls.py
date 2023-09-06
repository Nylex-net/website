from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # path originally '/home' instead of ''.
    path('home', views.home, name='home'),
    path('<slug:slug>', views.template, name='article')
]