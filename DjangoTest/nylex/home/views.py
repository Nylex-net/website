from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost

def home(request):
    content = BlogPost.objects.all()[0]
    context = {
        'content': content,
        'root': True
    }
    return HttpResponse(loader.get_template('home.html').render(context, request))