"""
There are different methods to get data from a model into a QuerySet.

THE VALUES() METHOD
=======================

The values() method allows you to return each object as a Python dictionary, with the names 
and values as key/value pairs:

from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
  
RETURN SPECIFI COLUMNS
=============================

The values_list() method allows you to return only the columns that you specify.

from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.values_list('firstname')
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
  
RETURN SPECIFIC ROWS
============================

You can filter the search to only return specific rows/records, by using the filter() method.

from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.filter(firstname='Emil').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
  

"""
