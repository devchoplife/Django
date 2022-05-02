"""
FILTER A VALUE 
=======================

With the pipe | character followed by a filter name, you can run a value through a filter 
before returning it.
The name of the filter defines what the filter will do with the value.

Example
+++++++++++++

Return the variable firstname with upper case letters:

<h1>Hello {{ firstname|upper }}, how are you?</h1>

THE FILTER TAG
===========================

The filter tag allows you to run a whole section of code through a filter, and return it 
according to the filter keyword(s).

Example
+++++++++++++

Return the variable firstname with upper case letters:

{% filter upper %}
  <h1>Hello everyone, how are you?</h1>
{% endfilter %}

To add multiple filters, separate the keywords with the pipe | character:

{% filter upper|linenumbers %}Hello!
my name is
Emil.
What is your name?{% endfilter %}
"""