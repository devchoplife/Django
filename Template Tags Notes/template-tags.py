"""`
In Django templates, you can perform programming logic like executing if statements and for loops.
These keywords, if and for, are called "template tags" in Django.
To execute template tags, we surrond them in {% %} brackets.

{% if greeting == 1 %}
  <h1>Hello</h1>
{% else %}
  <h1>Bye</h1>
{% endif %}

DJANGO CODE 
========================

The template tags are a way of telling Django that here comes something else than plain HTML.
The template tags allows us to to do some programming on the server before sending HTML to the client.

<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
  {% endfor %}
</ul>
"""