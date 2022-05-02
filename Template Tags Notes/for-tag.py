"""
A for loop is used for iterating over a sequence, like looping over items in an array, a list, or a dictionary.

{% for x in fruits %}
  <h1>{{ x }}</h1>
{% endfor %}

DATA FROM A MODEL
==========================

Data in a model is like a table with rows and columns.
The Members model we created earlier has five rows, and each row has three columns:

When we fetch data from the model, it comes as a QuerySet object, with a similar format as the 
cars example above: a list with dictionaries:

<QuerySet [
  {
    'id': 1,
    'firstname': 'Emil',
    'lastname': 'Refsnes'
  },
  {
    'id': 2,
    'firstname': 'Tobias',
    'lastname': 'Refsnes'
  },
  {
    'id': 3,
    'firstname': 'Linus',
    'lastname': 'Refsnes'
  },
  {
    'id': 4,
    'firstname': 'Lene',
    'lastname': 'Refsnes'
  },
  {
    'id': 5,
    'firstname': 'Stalikken',
    'lastname': 'Refsnes'
  }
]> 

Loop through items fetched from a database 

{% for x in members %}
  <h1>{{ x.id }}</h1>
  <p>
    {{ x.firstname }}
    {{ x.lastname }}
  </p>
{% endfor %} 

REVERSED
=====================

The reversed keyword is used when you want to do the loop in reversed order.

{% for x in members reversed %}
  <h1>{{ x.id }}</h1>
  <p>
    {{ x.firstname }}
    {{ x.lastname }}
  </p>
{% endfor %} 

EMPTY
====================

The empty keyword can be used if you want to do something special if the object is empty.

<ul>
  {% for x in emptytestobject %}
    <li>{{ x.firstname }}</li>
  {% empty %}
    <li>No members</li>
  {% endfor %}
</ul> 

The empty keyword can also be used if the object does not exist:

<ul>
  {% for x in myobject %}
    <li>{{ x.firstname }}</li>
  {% empty %}
    <li>No members</li>
  {% endfor %}
</ul> 

LOOP VARIABLES
===========================
Django has some variables that are available for you inside a loop:

- forloop.counter
- forloop.counter0
- forloop.first
- forloop.last
- forloop.parentloop
- forloop.revcounter
- forloop.revcounter0

FORLOOP.COUNTER
=====================

The current iteration, starting at 1.

<ul>
  {% for x in fruits %}
    <li>{{ forloop.counter }}</li>
  {% endfor %}
</ul> 

FORLOOP.COUNTER0
=======================

The current iteration, starting at 0.

<ul>
  {% for x in fruits %}
    <li>{{ forloop.counter0 }}</li>
  {% endfor %}
</ul> 

FORLOOP.FIRST
=========================

Allows you to test if the loop is on its first iteration.

<ul>
  {% for x in fruits %}
    <li
      {% if forloop.first %}
        style='background-color:lightblue;'
      {% endif %}
    >{{ x }}</li>
  {% endfor %}
</ul> 

FORLOOP.LAST 
=========================

Allows you to test if the loop is on its last iteration.

<ul>
  {% for x in fruits %}
    <li
      {% if forloop.last %}
        style='background-color:lightblue;'
      {% endif %}
    >{{ x }}</li>
  {% endfor %}
</ul> 

FORLOOP.REVCOUNTER
==========================

The current iteration if you start at the end and count backwards, ending up at 1.

<ul>
  {% for x in fruits %}
    <li>{{ forloop.revcounter }}</li>
  {% endfor %}
</ul> 

FORLOOP.REVCOUNTER0
===========================

The current iteration if you start at the end and count backwards, ending up at 0.

<ul>
  {% for x in fruits %}
    <li>{{ forloop.revcounter0 }}</li>
  {% endfor %}
</ul> 
"""
