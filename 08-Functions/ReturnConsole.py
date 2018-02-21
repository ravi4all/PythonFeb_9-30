Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Feb_2018/Python_Morning_9-30/08-Functions/04-DynamicArguments.py 
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Feb_2018/Python_Morning_9-30/08-Functions/04-DynamicArguments.py", line 7, in <module>
    emp("Ram",24,'Delhi', 'Noida')
TypeError: emp() takes 3 positional arguments but 4 were given
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Feb_2018/Python_Morning_9-30/08-Functions/04-DynamicArguments.py 
Name : Ram, age : 24
Address : ('Delhi', 'Noida')
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Feb_2018/Python_Morning_9-30/08-Functions/04-DynamicArguments.py 
Name : Ram, age : 24
Address : ('Delhi', 'Noida', 'Agra', 'Pune')
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Feb_2018/Python_Morning_9-30/08-Functions/04-DynamicArguments.py 
Name : Ram, age : 24
Address : ('Delhi', 'Noida', 'Agra', 'Pune')
{'name': 'HCL', 'branch': 'Noida', 'teamSize': 50}
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Feb_2018/Python_Morning_9-30/08-Functions/04-DynamicArguments.py 
Name : Ram, age : 24
Address : ('Delhi', 'Noida', 'Agra', 'Pune')
Details : {'name': 'HCL', 'branch': 'Noida', 'teamSize': 50}
Details : {'name': 'TCS', 'branch': 'Pune'}
>>> x = {'name': 'HCL', 'branch': 'Noida', 'teamSize': 50}
>>> x.get("name")
'HCL'
>>> x["name"]
'HCL'
>>> ch = {"1" : }
SyntaxError: invalid syntax
>>> def add():
	i = 10
	j = 12
	print("Addition is",i+j)

	
>>> def sub():
	i = 10
	j = 12
	print("Subtraction is",i-j)

	
>>> ch = {"1" : add(), "2" : sub()}
Addition is 22
Subtraction is -2
>>> userchoice = input("Enter your choice : ")
Enter your choice : 2
>>> ch.get(userchoice)
>>> ch.get(userchoice)
>>> ch = {"1" : add, "2" : sub}
>>> ch.get(userchoice)
<function sub at 0x000001EC7ABF27B8>
>>> sub
<function sub at 0x000001EC7ABF27B8>
>>> ch.get(userchoice)()
Subtraction is -2
>>> eval('12+12')
24
>>> eval('12-2')
10
>>> def show():
	print("Hello world")

	
>>> show()
Hello world
>>> x = show()
Hello world
>>> x
>>> print(x)
None
>>> print(show())
Hello world
None
>>> def show():
	x = 10
	print("Hello world")
	return x

>>> show()
Hello world
10
>>> x = show()
Hello world
>>> x
10
>>> type(x)
<class 'int'>
>>> def calc(x,y):
	return x+y, x-y, x/y, x*y

>>> calc(12,14)
(26, -2, 0.8571428571428571, 168)
>>> def calc(x,y):
	return x + y
	return x - y
	return x / y
	return x * y

>>> calc(12,11)
23
>>> def calc(x,y):
	return x+y, x-y, x/y, x*y

>>> a,b,c,d = calc(12,14)
>>> a
26
>>> b
-2
>>> c
0.8571428571428571
>>> d
168
>>> emp = name, age, address = "Ram", 25, 'Delhi'
>>> emp
('Ram', 25, 'Delhi')
>>> na
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    na
NameError: name 'na' is not defined
>>> name
'Ram'
>>> age]
SyntaxError: invalid syntax
>>> age
25
>>> address
'Delhi'
>>> values = a,b,c,d = calc(12,14)
>>> values
(26, -2, 0.8571428571428571, 168)
>>> a
26
>>> b
-2
>>> c
0.8571428571428571
>>> d
168
>>> 
