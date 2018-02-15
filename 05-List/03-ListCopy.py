Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list_1 = [12,34,56,11,15,5,45,23]
>>> 12 in list_1
True
>>> list_2 = list_1
>>> list_1[0] = 'Hi'
>>> list_1
['Hi', 34, 56, 11, 15, 5, 45, 23]
>>> list_2
['Hi', 34, 56, 11, 15, 5, 45, 23]
>>> list_3 = list_1[:]
>>> list_1 == list_2
True
>>> list_1 == list_3
True
>>> list_1 is list_2
True
>>> list_1 is list_3
False
>>> list_1[0] = 'Bye'
>>> list_2
['Bye', 34, 56, 11, 15, 5, 45, 23]
>>> list_3
['Hi', 34, 56, 11, 15, 5, 45, 23]
>>> list_1.append(['Hey','Python','Bye'])
>>> list_1
['Bye', 34, 56, 11, 15, 5, 45, 23, ['Hey', 'Python', 'Bye']]
>>> list_2
['Bye', 34, 56, 11, 15, 5, 45, 23, ['Hey', 'Python', 'Bye']]
>>> list_3
['Hi', 34, 56, 11, 15, 5, 45, 23]
>>> list_4 = list_1[:]
>>> list_4
['Bye', 34, 56, 11, 15, 5, 45, 23, ['Hey', 'Python', 'Bye']]
>>> list_1[-1][0] = 'Hello'
>>> list_1
['Bye', 34, 56, 11, 15, 5, 45, 23, ['Hello', 'Python', 'Bye']]
>>> list_4
['Bye', 34, 56, 11, 15, 5, 45, 23, ['Hello', 'Python', 'Bye']]
>>> list_1[0] = 'Python'
>>> list_1
['Python', 34, 56, 11, 15, 5, 45, 23, ['Hello', 'Python', 'Bye']]
>>> list_4
['Bye', 34, 56, 11, 15, 5, 45, 23, ['Hello', 'Python', 'Bye']]
>>> list_1[-1][0] = 'Bye'
>>> list_1
['Python', 34, 56, 11, 15, 5, 45, 23, ['Bye', 'Python', 'Bye']]
>>> list_4
['Bye', 34, 56, 11, 15, 5, 45, 23, ['Bye', 'Python', 'Bye']]
>>> import copy
>>> list_5 = copy.deepcopy(list_1)
>>> list_5
['Python', 34, 56, 11, 15, 5, 45, 23, ['Bye', 'Python', 'Bye']]
>>> list_1[-1][0] = 'Hello'
>>> list_1
['Python', 34, 56, 11, 15, 5, 45, 23, ['Hello', 'Python', 'Bye']]
>>> list_5
['Python', 34, 56, 11, 15, 5, 45, 23, ['Bye', 'Python', 'Bye']]
>>> 
