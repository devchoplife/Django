"""
Comments allows you to have sections of code that should be ignored.

<h1>Welcome Everyone</h1>
{% comment %}
  <h1>Welcome ladies and gentlemen</h1>
{% endcomment %}

COMMENT DESCRIPTION
======================

You can add a message to your comment, to help you remember why you wrote the comment, or as 
message to other people reading the code.

<h1>Welcome Everyone</h1>
{% comment "this was the original welcome message" %}
    <h1>Welcome ladies and gentlemen</h1>
{% endcomment %}

SMALLER COMMENTS
======================

You can also use the {# ... #} tags when commenting out code, which can be easier when for 
smaller comments:

<h1>Welcome{# Everyone#}</h1>

COMMENT IN VIEWS
=======================

Views are written in Python, and Python comments are written with the # character:

from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  #context = {
  # 'var1': 'John',
  #}
  return HttpResponse(template.render())
  

"""
