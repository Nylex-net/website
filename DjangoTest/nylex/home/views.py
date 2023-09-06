from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.template import loader
from .models import Page

def home(request):
    content = Page.objects.all()[0]
    context = {
        'content': content
    }
    return HttpResponse(loader.get_template('home.html').render(context, request))

def template(request, slug):
    content = Page.objects.filter(title=slug)
    if len(content) <= 0:
        print("0 results from " + slug)
        home(request)
        return
    else:
        content = content.all().values()[0]
        context = {
            'content': content
        }
        return HttpResponse(loader.get_template('template.html').render(context, request))