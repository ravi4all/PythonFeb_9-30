Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> user = []
>>> username = 'Ram'
>>> user[0] = username
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    user[0] = username
IndexError: list assignment index out of range
>>> user.append(username)
>>> user
['Ram']
>>> username = 'Shyam'
>>> user.append(username)
>>> user
['Ram', 'Shyam']
>>> for i in range(5):
	username = input("Enter username : ")
	user.append(username)

	
Enter username : John
Enter username : Ravi
Enter username : Amit
Enter username : Mohan
Enter username : Ajay
>>> user
['Ram', 'Shyam', 'John', 'Ravi', 'Amit', 'Mohan', 'Ajay']
>>> user[0]
'Ram'
>>> user.append('Atul','Gopal','Pooja')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    user.append('Atul','Gopal','Pooja')
TypeError: append() takes exactly one argument (3 given)
>>> user.append(['Pune','Mumbai','Delhi','Agra','Pune','Kolkata','Delhi'])
>>> user
['Ram', 'Shyam', 'John', 'Ravi', 'Amit', 'Mohan', 'Ajay', ['Pune', 'Mumbai', 'Delhi', 'Agra', 'Pune', 'Kolkata', 'Delhi']]
>>> user[-1]
['Pune', 'Mumbai', 'Delhi', 'Agra', 'Pune', 'Kolkata', 'Delhi']
>>> user[-1][0]
'Pune'
>>> print(user[0], user[-1][0])
Ram Pune
>>> for i in range(len(user)):
	print(user[i], user[-1][i])

	
Ram Pune
Shyam Mumbai
John Delhi
Ravi Agra
Amit Pune
Mohan Kolkata
Ajay Delhi
Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    print(user[i], user[-1][i])
IndexError: list index out of range
>>> print(user[:], user[::-1])
['Ram', 'Shyam', 'John', 'Ravi', 'Amit', 'Mohan', 'Ajay', ['Pune', 'Mumbai', 'Delhi', 'Agra', 'Pune', 'Kolkata', 'Delhi']] [['Pune', 'Mumbai', 'Delhi', 'Agra', 'Pune', 'Kolkata', 'Delhi'], 'Ajay', 'Mohan', 'Amit', 'Ravi', 'John', 'Shyam', 'Ram']
>>> user.pop()
['Pune', 'Mumbai', 'Delhi', 'Agra', 'Pune', 'Kolkata', 'Delhi']
>>> user
['Ram', 'Shyam', 'John', 'Ravi', 'Amit', 'Mohan', 'Ajay']
>>> user.pop()
'Ajay'
>>> user
['Ram', 'Shyam', 'John', 'Ravi', 'Amit', 'Mohan']
>>> user.pop(4)
'Amit'
>>> user
['Ram', 'Shyam', 'John', 'Ravi', 'Mohan']
>>> user.remove(3)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    user.remove(3)
ValueError: list.remove(x): x not in list
>>> user.remove('Ravi')
>>> user
['Ram', 'Shyam', 'John', 'Mohan']
>>> user[0] = 'Ravi'
>>> user
['Ravi', 'Shyam', 'John', 'Mohan']
>>> user.insert(1,'Ram')
>>> user
['Ravi', 'Ram', 'Shyam', 'John', 'Mohan']
>>> new_users = ['Pooja','Jyoti','Astha','Meena','Sita']
>>> user + new_users
['Ravi', 'Ram', 'Shyam', 'John', 'Mohan', 'Pooja', 'Jyoti', 'Astha', 'Meena', 'Sita']
>>> user = user + new_users
>>> user
['Ravi', 'Ram', 'Shyam', 'John', 'Mohan', 'Pooja', 'Jyoti', 'Astha', 'Meena', 'Sita']
>>> user.pop()
'Sita'
>>> city = ['Delhi','Mumbai','Agra','Pune']
>>> user.extend(city)
>>> user
['Ravi', 'Ram', 'Shyam', 'John', 'Mohan', 'Pooja', 'Jyoti', 'Astha', 'Meena', 'Delhi', 'Mumbai', 'Agra', 'Pune']
>>> user.count('Ram')
1
>>> user.index('Agra')
11
>>> sorted(user)
['Agra', 'Astha', 'Delhi', 'John', 'Jyoti', 'Meena', 'Mohan', 'Mumbai', 'Pooja', 'Pune', 'Ram', 'Ravi', 'Shyam']
>>> sorted(user, reverse = True)
['Shyam', 'Ravi', 'Ram', 'Pune', 'Pooja', 'Mumbai', 'Mohan', 'Meena', 'Jyoti', 'John', 'Delhi', 'Astha', 'Agra']
>>> sorted_userList = sorted(user)
>>> user
['Ravi', 'Ram', 'Shyam', 'John', 'Mohan', 'Pooja', 'Jyoti', 'Astha', 'Meena', 'Delhi', 'Mumbai', 'Agra', 'Pune']
>>> user.sort()
>>> user
['Agra', 'Astha', 'Delhi', 'John', 'Jyoti', 'Meena', 'Mohan', 'Mumbai', 'Pooja', 'Pune', 'Ram', 'Ravi', 'Shyam']
>>> user.append(12)
>>> user.append(23)
>>> user.append(15)
>>> user
['Agra', 'Astha', 'Delhi', 'John', 'Jyoti', 'Meena', 'Mohan', 'Mumbai', 'Pooja', 'Pune', 'Ram', 'Ravi', 'Shyam', 12, 23, 15]
>>> user.sort()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    user.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> user.clear()
>>> user
[]
>>> user.append(['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta'],['Delhi', 'Mumbai', 'Agra', 'Pune','Delhi'],['M','M','M','F','F'])
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    user.append(['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta'],['Delhi', 'Mumbai', 'Agra', 'Pune','Delhi'],['M','M','M','F','F'])
TypeError: append() takes exactly one argument (3 given)
>>> user.append(['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta'])
>>> user
[['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta']]
>>> user.append(['Delhi', 'Mumbai', 'Agra', 'Pune','Delhi'])
>>> user
[['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta'], ['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi']]
>>> user.append(['M','M','M','F','F'])
>>> user
[['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta'], ['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi'], ['M', 'M', 'M', 'F', 'F']]
>>> user[0]
['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta']
>>> user[1]
['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi']
>>> user[2]
['M', 'M', 'M', 'F', 'F']
>>> user[0][2]
'Shyam'
>>> user[0].append('Jyoti')
>>> user
[['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta', 'Jyoti'], ['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi'], ['M', 'M', 'M', 'F', 'F']]
>>> user[1].append('Punjab')
>>> user[2].append('F')
>>> user
[['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta', 'Jyoti'], ['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi', 'Punjab'], ['M', 'M', 'M', 'F', 'F', 'F']]
>>> for data in user:
	print(data)

	
['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta', 'Jyoti']
['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi', 'Punjab']
['M', 'M', 'M', 'F', 'F', 'F']
>>> for i in range(len(user)):
	print(user[i][i])

	
Ravi
Mumbai
M
>>> for row in range(0,len(user)):
	for col in user[row]:
		print(user[row][col])

		
Traceback (most recent call last):
  File "<pyshell#84>", line 3, in <module>
    print(user[row][col])
TypeError: list indices must be integers or slices, not str
>>> for row in range(0,len(user)):
	for col in range(0,len(user[row])):
		print(user[row][col])

		
Ravi
Ram
Shyam
Pooja
Ekta
Jyoti
Delhi
Mumbai
Agra
Pune
Delhi
Punjab
M
M
M
F
F
F
>>> for row in range(0,len(user)):
	for col in range(0,len(user[row])):
		print(user[row][0])

		
Ravi
Ravi
Ravi
Ravi
Ravi
Ravi
Delhi
Delhi
Delhi
Delhi
Delhi
Delhi
M
M
M
M
M
M
>>> for row in range(0,len(user)):
	for col in range(0,7):
		print(user[row][col])

		
Ravi
Ram
Shyam
Pooja
Ekta
Jyoti
Traceback (most recent call last):
  File "<pyshell#90>", line 3, in <module>
    print(user[row][col])
IndexError: list index out of range
>>> for row in range(0,len(user)):
	for col in range(0,7):
		print(user[row])

		
['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta', 'Jyoti']
['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta', 'Jyoti']
['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta', 'Jyoti']
['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta', 'Jyoti']
['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta', 'Jyoti']
['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta', 'Jyoti']
['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta', 'Jyoti']
['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi', 'Punjab']
['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi', 'Punjab']
['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi', 'Punjab']
['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi', 'Punjab']
['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi', 'Punjab']
['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi', 'Punjab']
['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi', 'Punjab']
['M', 'M', 'M', 'F', 'F', 'F']
['M', 'M', 'M', 'F', 'F', 'F']
['M', 'M', 'M', 'F', 'F', 'F']
['M', 'M', 'M', 'F', 'F', 'F']
['M', 'M', 'M', 'F', 'F', 'F']
['M', 'M', 'M', 'F', 'F', 'F']
['M', 'M', 'M', 'F', 'F', 'F']
>>> for row in range(0,len(user)):
	for col in range(0,row):
		print(user[row][col])

		
Delhi
M
M
>>> for row in range(0,len(user)):
	for col in range(0,3):
		print(user[col][row], end='')

		
RaviDelhiMRamMumbaiMShyamAgraM
>>> for row in range(0,len(user)):
	for col in range(0,3):
		print(user[col][row], end=' ')

		
Ravi Delhi M Ram Mumbai M Shyam Agra M 
>>> for row in range(0,len(user)):
	for col in range(0,3):
		print(user[col][row], end=' ')
	print()

	
Ravi Delhi M 
Ram Mumbai M 
Shyam Agra M 
>>> for row in range(0,len(user)):
	for col in range(0,7):
		print(user[col][row], end=' ')
	print()

	
Ravi Delhi M Traceback (most recent call last):
  File "<pyshell#103>", line 3, in <module>
    print(user[col][row], end=' ')
IndexError: list index out of range
>>> for row in range(0,len(user)):
	for col in range(0,4):
		print(user[col][row], end=' ')
	print()

	
Ravi Delhi M Traceback (most recent call last):
  File "<pyshell#105>", line 3, in <module>
    print(user[col][row], end=' ')
IndexError: list index out of range
>>> for row in range(0,len(user)):
	for col in range(0,3):
		print(user[col][row], end=' ')
	print()

	
Ravi Delhi M 
Ram Mumbai M 
Shyam Agra M 
>>> for row in range(0,len(user)):
	for col in range(0,len(user[row])):
		print(user[row][0])

		
Ravi
Ravi
Ravi
Ravi
Ravi
Ravi
Delhi
Delhi
Delhi
Delhi
Delhi
Delhi
M
M
M
M
M
M
>>> user
[['Ravi', 'Ram', 'Shyam', 'Pooja', 'Ekta', 'Jyoti'], ['Delhi', 'Mumbai', 'Agra', 'Pune', 'Delhi', 'Punjab'], ['M', 'M', 'M', 'F', 'F', 'F']]
>>> user[0][0]
'Ravi'
>>> user[0][1]
'Ram'
>>> user[1][0]
'Delhi'
>>> user[2][0]
'M'
>>> print(user[0][0], user[1][0], user[2][0])
Ravi Delhi M
>>> print(user[0][1], user[1][1], user[2][1])
Ram Mumbai M
>>> 
>>> print(user[0][2], user[1][2], user[2][2])
Shyam Agra M
>>> for row in range(0, len(user))
SyntaxError: invalid syntax
>>> for row in range(0, len(user[0])):
	for col in range(0,row):
		print(user[0][row])

		
Ram
Shyam
Shyam
Pooja
Pooja
Pooja
Ekta
Ekta
Ekta
Ekta
Jyoti
Jyoti
Jyoti
Jyoti
Jyoti
>>> for row in range(0, len(user[0])):
	for col in range(0,3):
		print(user[col][row], end = ' ')
	print()

	
Ravi Delhi M 
Ram Mumbai M 
Shyam Agra M 
Pooja Pune F 
Ekta Delhi F 
Jyoti Punjab F 
>>> 
