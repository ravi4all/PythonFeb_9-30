Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict_1 = {'name':'Ram','age':23,'salary':15000}
>>> dict_1
{'name': 'Ram', 'age': 23, 'salary': 15000}
>>> dict_1[0]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    dict_1[0]
KeyError: 0
>>> dict_1['name']
'Ram'
>>> dict_1.keys()
dict_keys(['name', 'age', 'salary'])
>>> dict_1.values()
dict_values(['Ram', 23, 15000])
>>> dict_1.items()
dict_items([('name', 'Ram'), ('age', 23), ('salary', 15000)])
>>> dict_1['company'] = 'HCL'
>>> dict_1
{'name': 'Ram', 'age': 23, 'salary': 15000, 'company': 'HCL'}
>>> emp = {'name' : ['Ram','Shyam','Gopal'], 'age' : [23,25,27], 'salary' : [18000,25000,70000]}
>>> emp
{'name': ['Ram', 'Shyam', 'Gopal'], 'age': [23, 25, 27], 'salary': [18000, 25000, 70000]}
>>> emp['name']
['Ram', 'Shyam', 'Gopal']
>>> emp['name'][3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    emp['name'][3]
IndexError: list index out of range
>>> emp['name'][2]
'Gopal'
>>> emp['name'].append('Ajay')
>>> emp['age'].append(30)
>>> emp['salary'].append()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    emp['salary'].append()
TypeError: append() takes exactly one argument (0 given)
>>> 
>>> emp['salary'].append(50000)
>>> emp
{'name': ['Ram', 'Shyam', 'Gopal', 'Ajay'], 'age': [23, 25, 27, 30], 'salary': [18000, 25000, 70000, 50000]}
>>> print(emp[0][0], emp[1][0], emp[2][0])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(emp[0][0], emp[1][0], emp[2][0])
KeyError: 0
>>> print(emp['name'][0], emp['age'][0], emp['salary'][0])
Ram 23 18000
>>> print(emp['name'][1], emp['age'][1], emp['salary'][2])
Shyam 25 70000
>>> for i in range(len(emp)):
	print(emp['name'][i])

	
Ram
Shyam
Gopal
>>> for i in range(len(emp)):
	print(emp['name'][i], emp['age'][i], emp['salary'][i])

	
Ram 23 18000
Shyam 25 25000
Gopal 27 70000
>>> for i in range(len(emp['name'])):
	print(emp['name'][i], emp['age'][i], emp['salary'][i])

	
Ram 23 18000
Shyam 25 25000
Gopal 27 70000
Ajay 30 50000
>>> data = [{'name' : 'Ram', 'age' : 16, 'course':'Btech'},{'name' : 'Shyam', 'age' : 18, 'course':'BCA'},{'name' : 'Anuj', 'age' : 20, 'course':'Btech'},{'name' : 'Ankur', 'age' : 17, 'course':'BCA'}]
>>> for students in data:
	print(students)

	
{'name': 'Ram', 'age': 16, 'course': 'Btech'}
{'name': 'Shyam', 'age': 18, 'course': 'BCA'}
{'name': 'Anuj', 'age': 20, 'course': 'Btech'}
{'name': 'Ankur', 'age': 17, 'course': 'BCA'}
>>> emp
{'name': ['Ram', 'Shyam', 'Gopal', 'Ajay'], 'age': [23, 25, 27, 30], 'salary': [18000, 25000, 70000, 50000]}
>>> dict_1
{'name': 'Ram', 'age': 23, 'salary': 15000, 'company': 'HCL'}
>>> for data in dict_1:
	print(data)

	
name
age
salary
company
>>> for data in dict_1.values():
	print(data)

	
Ram
23
15000
HCL
>>> for data in dict_1.items():
	print(data)

	
('name', 'Ram')
('age', 23)
('salary', 15000)
('company', 'HCL')
>>> data
('company', 'HCL')
>>> data = [{'name' : 'Ram', 'age' : 16, 'course':'Btech'},{'name' : 'Shyam', 'age' : 18, 'course':'BCA'},{'name' : 'Anuj', 'age' : 20, 'course':'Btech'},{'name' : 'Ankur', 'age' : 17, 'course':'BCA'}]
>>> data
[{'name': 'Ram', 'age': 16, 'course': 'Btech'}, {'name': 'Shyam', 'age': 18, 'course': 'BCA'}, {'name': 'Anuj', 'age': 20, 'course': 'Btech'}, {'name': 'Ankur', 'age': 17, 'course': 'BCA'}]
>>> sorted(data)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    sorted(data)
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> sorted(data, key='name')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    sorted(data, key='name')
TypeError: 'str' object is not callable
>>> def sort_emp(key):
	return emp[key]

>>> sorted(data, key=sort_emp)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    sorted(data, key=sort_emp)
  File "<pyshell#50>", line 2, in sort_emp
    return emp[key]
TypeError: unhashable type: 'dict'
>>> sorted(data, key=lambda x : x['name'])
[{'name': 'Ankur', 'age': 17, 'course': 'BCA'}, {'name': 'Anuj', 'age': 20, 'course': 'Btech'}, {'name': 'Ram', 'age': 16, 'course': 'Btech'}, {'name': 'Shyam', 'age': 18, 'course': 'BCA'}]
>>> 
