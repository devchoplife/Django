"""
In Django templates, you can render variables by putting them inside {{ }} brackets:

<h1>Hello {{ firstname }}, how are you?</h1>

The variable firstname in the example above was sent to the template via a view:

from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'firstname': 'Linus',
  }
  return HttpResponse(template.render(context, request))
  
As you can see in the view above, we create an object named context and fill it with data, 
and send it as the first parameter in the template.render() function.

CREATE VARIABLES IN TEMPLATE
============================================

{% with firstname="Tobias" %}
<h1>Hello {{ firstname }}, how are you?</h1>


DATA FROM A MODEL
==========================================

The example above showed a easy approach on how to create and use variables in a template.
Normally, most of the external data you want to use in a template, comes from a model.
We have created a model in the previous chapters, called Members, we will use this model in the next chapters of this tutorial.
To get data from the Memebers model, we will have to import it in the views file, and extract data from it in the view:

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members

def testing(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  

Now we can use the data in the template:

<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
  {% endfor %}
</ul>

We use the Django template tag {% for %} to loop through the members.
"""