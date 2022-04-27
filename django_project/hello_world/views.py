"""
Django views are Python functions that takes http requests and returns http response, like HTML documents.
A web page that uses Django is full of views with different tasks and missions.
Views are usually put in a file called views.py located on your app's folder
"""
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")