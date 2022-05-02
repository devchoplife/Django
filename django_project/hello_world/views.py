"""
Django views are Python functions that takes http requests and returns http response, like HTML documents.
A web page that uses Django is full of views with different tasks and missions.
Views are usually put in a file called views.py located on your app's folder
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from hello_world.models import HelloUsers


def index(request):
    Myusers = HelloUsers.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'Myusers': Myusers,
    }

    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']

    user = HelloUsers(firstname=x, lastname=y)
    user.save()

    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    user = HelloUsers.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    user = HelloUsers.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'Myusers': user
    }

    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']

    user = HelloUsers.objects.get(id=id)
    user.firstname = first
    user.lastname = last
    user.save()

    return HttpResponseRedirect(reverse('index'))
