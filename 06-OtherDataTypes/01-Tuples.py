Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list_1 = [2,3,4,6,1,2,8,9,7]
>>> tup_1 = (1,2,8,9,7,'Hi','Hello','Bye',12.5)
>>> tup_1[3]
9
>>> tup_1[-1]
12.5
>>> tup[0:6]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tup[0:6]
NameError: name 'tup' is not defined
>>> tup_1[0:6]
(1, 2, 8, 9, 7, 'Hi')
>>> tup_1[::-1]
(12.5, 'Bye', 'Hello', 'Hi', 7, 9, 8, 2, 1)
>>> type(tup_1)
<class 'tuple'>
>>> tup_1[0] = 'Bye'
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tup_1[0] = 'Bye'
TypeError: 'tuple' object does not support item assignment
>>> emp = name,age,salary = 'Ram', 23, 15000
>>> emp
('Ram', 23, 15000)
>>> name
'Ram'
>>> age
23
>>> salary
15000
>>> employees = []
>>> employees.append(emp)
>>> employees
[('Ram', 23, 15000)]
>>> emp = name,age,salary = 'Shyam', 27, 35000
>>> employees.append(emp)
>>> emp
('Shyam', 27, 35000)
>>> emp = 'Ram', 23, 15000
>>> emp
('Ram', 23, 15000)
>>> name, age, salary = emp
>>> name
'Ram'
>>> age
23
>>> salary
15000
>>> 
