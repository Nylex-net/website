from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Page

def home(request):
    content = Page.objects.all()[0]
    context = {
        'content': content,
        'root': True
    }
    return HttpResponse(loader.get_template('home.html').render(context, request))

def page(request, page_id):
    content = Page.objects.get(pk=page_id)
    context = {
        'content': content,
        'root': False
    }
    return HttpResponse(loader.get_template('template.html').render(context, request))