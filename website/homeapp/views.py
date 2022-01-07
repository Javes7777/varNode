from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_projects(request):
    return HttpResponse('These are my projects:')

def blogs(request):
    return HttpResponse('This is blog:')

def index(request):
    return HttpResponse('Hello, world! home page')