"""
The filter() method is used to filter your search, and allows you to return only the rows 
that matches the search term.
As we learned in the previous chapter, we can filter on field names like this:

mydata = Members.objects.filter(firstname='Emil').values()

In SQL, the above statement would be written like this:

SELECT * FROM members WHERE firstname = 'Emil';

AND
=====

The filter() method takes the arguments as **kwargs (keyword arguments), so you can filter on more than one field by sepearting them by a comma.

mydata = Members.objects.filter(lastname='Refsnes', id=2).values()

In SQL, the above statement would be written like this:

SELECT * FROM members WHERE   lastname = 'Refsnes' AND id = 2;

OR
======

To return records where firstname is Emil or firstname is Tobias (meaning: returning records 
that matches either query, not necessarily both) is not as easy as the AND example above.

We can use multiple filter() methods, separated by a pipe | character. The results will 
merge into one model.

mydata = Members.objects.filter(firstname='Emil').values() | Members.objects.filter(firstname='Tobias').values()

Another common method is to import and use Q expressions:

from django.http import HttpResponse
from django.template import loader
from .models import Members
from django.db.models import Q

def testing(request):
  mydata = Members.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
  
In SQL, the above statement would be written like this:

SELECT * FROM members WHERE   firstname = 'Emil' OR firstname = 'Tobias';

FIELD LOOKUPS
====================

Django has its own way of specifying SQL statements and WHERE clauses.
To make specific where clasuses in Django, use "Field lookups".
Field lookups are keywords that represents specific SQL keywords.

Example:
+++++++++++++

.filter(firstname__startswith='L');

Is the same as the SQL statment:

WHERE firstname LIKE '%L'

FIELD LOOKUPS SYNTAX
=====================

All Field lookup keywords must be specified with the fieldname, followed by two(!) 
underscore characters, and the keyword.

In our Members model, the statement would be written like this:

mydata = Members.objects.filter(firstname__startswith='L').values()
"""
