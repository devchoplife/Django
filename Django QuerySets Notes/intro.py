"""
A QuerySet is a collection of data from a database.
A QuerySet is built up as a list of objects.
QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data.
In this tutorial we will be querying data from the Members table

QUERYING DATA
==================

In views.py, we have a view for testing called testing where we will test 
different queries.
In the example below we use the .all() method to get all the records and 
fields of the Members model:

from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.all()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
  

The object is placed in a variable called mydata, and is sent to the template 
via the context object as mymembers, and looks like this:

In the template you can use the mymembers object to generate content:

<table border='1'>
  <tr>
    <th>ID</th>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
  {% for x in mymembers %}
    <tr>
      <td>{{ x.id }}</td>
        <td>{{ x.firstname }}</td>
      <td>{{ x.lastname }}</td>
    </tr>
  {% endfor %}
</table>
"""
