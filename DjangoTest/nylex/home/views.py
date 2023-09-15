from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.db.models import Q
from .models import Page
import re

def home(request):
    content = Page.objects.filter(slug='home')
    if len(content) <= 0:
        print("No home menu")
        # home(request)
        return HttpResponseNotFound(loader.get_template('404.html').render(None, request))
    else:
        content = content.all().values()[0]
        context = {
            'content': content
        }
        return HttpResponse(loader.get_template('home.html').render(context, request))

def template(request, slug):
    content = Page.objects.filter(slug=slug)
    if len(content) <= 0:
        print("0 results from " + slug)
        # home(request)
        return HttpResponseNotFound(loader.get_template('404.html').render(None, request))
    else:
        content = content.all().values()[0]
        context = {
            'content': content
        }
        return HttpResponse(loader.get_template('template.html').render(context, request))
    
def search(request):
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        posts = Page.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query) | Q(header__icontains=search_query))
        for post in posts:
            post.content = re.sub(r'<.*?>', '', post.content)
        context = {'query':search_query, 'posts':posts}
        return HttpResponse(loader.get_template('search.html').render(context, request))
    else:
        return HttpResponse(loader.get_template('search.html').render({}, request))
    
def site_map(request):
    posts = Page.objects.all().order_by('title')
    for post in posts:
        post.content = re.sub(r'<.*?>', '', post.content)
    context = {'posts':posts}
    return HttpResponse(loader.get_template('site-map.html').render(context, request))