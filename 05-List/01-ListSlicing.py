Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list_1 = [1,2,3,4,5,6'Hi',10.56,True]
SyntaxError: invalid syntax
>>> list_1 = [1,2,3,4,5,6,'Hi',10.56,True]
>>> list
<class 'list'>
_
>>> list_1[0]
1
>>> list_1[5]
6
>>> list_1[9]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list_1[9]
IndexError: list index out of range
>>> list_1[-1]
True
>>> list_1[-2]
10.56
>>> list_1
[1, 2, 3, 4, 5, 6, 'Hi', 10.56, True]
>>> list_1[0:5]
[1, 2, 3, 4, 5]
>>> list_1[3:8]
[4, 5, 6, 'Hi', 10.56]
>>> list_1[0:-1]
[1, 2, 3, 4, 5, 6, 'Hi', 10.56]
>>> list_1[0:8:2]
[1, 3, 5, 'Hi']
>>> list_1[0:]
[1, 2, 3, 4, 5, 6, 'Hi', 10.56, True]
>>> list_1[:-1]
[1, 2, 3, 4, 5, 6, 'Hi', 10.56]
>>> list_1[0:100]
[1, 2, 3, 4, 5, 6, 'Hi', 10.56, True]
>>> list_1[:]
[1, 2, 3, 4, 5, 6, 'Hi', 10.56, True]
>>> list_1[::]
[1, 2, 3, 4, 5, 6, 'Hi', 10.56, True]
>>> list[::-1]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    list[::-1]
TypeError: 'type' object is not subscriptable
>>> list_1[::-1]
[True, 10.56, 'Hi', 6, 5, 4, 3, 2, 1]
>>> x = "Hello world this is python"
>>> x[0:10]
'Hello worl'
>>> x[::-1]
'nohtyp si siht dlrow olleH'
>>> 
