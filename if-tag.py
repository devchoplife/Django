"""
IF STATEMENT
===============================

{% if greeting == 1 %}
  <h1>Hello</h1>
{% endif %} 

ELIF
================================

{% if greeting == 1 %}
  <h1>Hello</h1>
{% elif greeting == 2 %}
  <h1>Welcome</h1>
{% endif %} 

ELSE
=========================

{% if greeting == 1 %}
  <h1>Hello</h1>
{% elif greeting == 2 %}
  <h1>Welcome</h1>
{% else %}
  <h1>Goodbye</h1>
{% endif %} 

OPERATORS
==============================

The above examples uses the == operator, which is used to check if a variable is equal to a 
value, but there are many other operators you can use, or you can even drop the operator if 
you just want to check if a variable is not empty:

{% if greeting %}
  <h1>Hello</h1>
{% endif %} 

==
========================

{% if greeting == 2 %}
  <h1>Hello</h1>
{% endif %} 

!=
======================

{% if greeting != 1 %}
  <h1>Hello</h1>
{% endif %} 

<
==================

{% if greeting < 3 %}
  <h1>Hello</h1>
{% endif %} 

>
=========================

{% if greeting > 1 %}
  <h1>Hello</h1>
{% endif %} 

<=
======================

{% if greeting <= 3 %}
  <h1>Hello</h1>
{% endif %} 

>=
========================

{% if greeting >= 1 %}
  <h1>Hello</h1>
{% endif %} 

AND
=======================

{% if greeting == 1 and day == "Friday" %}
  <h1>Hello Weekend!</h1>
{% endif %} 

OR
======================

{% if greeting == 1 or greeting == 5 %}
  <h1>Hello</h1>
{% endif %} 

AND/OR
======================

{% if greeting == 1 and day == "Friday" or greeting == 5 %}

Parentheses are not allowed in if statements in Django, so when you combine and and or 
operators, it is important to know that parentheses are added for and but not for or.
Meaning that the above example is read by the interpreter like this:

{% if (greeting == 1 and day == "Friday") or greeting == 5 %}

IN
======================

{% if 'Banana' in fruits %}
  <h1>Hello</h1>
{% else %}
  <h1>Goodbye</h1>
{% endif %} 

NOT IN
=======================

{% if 'Banana' not in fruits %}
  <h1>Hello</h1>
{% else %}
  <h1>Goodbye</h1>
{% endif %} 

IS
======================

Check if two objects are the same.
This operator is different from the == operator, because the == operator checks the values of 
two objects, but the is operator checks the identity of two objects.
In the view we have two objects, x and y, with the same values:

from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'], 
  }

How can two objects be the same? Well, if you have two objects that points to the same object, then the is operator evaluates to true:
We will demonstrate this by using the {% with %} tag, which allows us to create variables in the template:

{% with var1=x var2=x %}
  {% if var1 == var2 %}
    <h1>YES</h1>
  {% else %}
    <h1>NO</h1>
  {% endif %}
{% endwith %}

IS NOT
==================

{% if x is not y %}
  <h1>YES</h1>
{% else %}
  <h1>NO</h1>
{% endif %} 
"""