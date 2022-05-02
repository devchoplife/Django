"""
CYCLES
====================

The cycle tag allows you to do different tasks for different iterations.

The cycle tag takes arguments, the first iteration uses the first argument, 
the second iteration uses the second argument etc.

{% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' %}

If you want to have a new background color for each iteration, you can do that with the cycle tag:

<ul>
  {% for x in members %}
    <li style='background-color:{% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' %}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul> 

If the cycle reaches the end of the arguments, it starts over:

CYCLE ARGUMENTS AS VARIABLES
==============================

In the first example the argument values was displayed directly in the cycle, but you can also 
keep the argument values in a variable, and use it later:

<ul>
  {% for x in members %}
    {% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' as bgcolor silent %}
    <li style='background-color:{{ bgcolor }}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul> 

Did you notice the silent keyword? Make sure you add this, or else the argument values will be 
displayed twice in the output:

RESET CYCLE
========================

You can force the cycle to restart by using the {% resetcycle %} tag:

<ul>
  {% for x in members %}
    {% cycle 'lightblue' 'pink' 'yellow' 'coral' 'grey' as bgcolor silent %}
    {% if forloop.counter == 3 %}
      {% resetcycle %}
    {% endif %}
    <li style='background-color:{{ bgcolor }}'>
      {{ x.firstname }}
    </li>
  {% endfor %}
</ul> 
"""