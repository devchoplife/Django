"""
To sort QuerySets, Django uses the order_by() method:

mydata = Members.objects.all().order_by('firstname').values()

In SQL, the above statement would be written like this:

SELECT * FROM members ORDER BY firstname;

DESCENDING ORDER
=======================

By default, the result is sorted ascending (the lowest value first), to change the direction 
to descending (the highest value first), use the minus sign (NOT), - in front of the field 
name:

mydata = Members.objects.all().order_by('-firstname').values()

In SQL, the above statement would be written like this:

SELECT * FROM members ORDER BY firstname DESC;

MULTIPLE ORDER BYS
======================

To order by more than one field, separate the fieldnames with a comma in the order_by() 
method:

mydata = Members.objects.all().order_by('lastname', '-id').values()

In SQL, the above statement would be written like this:

SELECT * FROM members ORDER BY lastname ASC, id DESC;
"""
