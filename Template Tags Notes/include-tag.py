"""
The include tag allows you include a template inside the current template.
This is useful when you have a block of content that are the same for many pages.

Example
++++++++++++

Footer
---------------
<p>You have reach the bottom of this page, thank you for your time.</p>

Template
-----------------
<h1>Hello</h1>
<p>This page contains a footer in a template.</p>
{% include 'footer.html' %} 

VARIATIIONS IN INCLUDE
=========================

You can send variables into the template by using the with keyword.
In the include file, you refer to the variables by using the {{ variablename }} syntax:

menu.html
-------------------
<div>HOME | {{ me }} | ABOUT | FORUM | {{ sponsor }}</div>

template.html
--------------------
<!DOCTYPE html>
<html>
<body>

{% include mymenu.html with me="TOBIAS" sponsor="W3SCHOOLS" %}

<h1>Welcome</h1>

<p>This is my webpage</p>

</body>
</html> 
"""