Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def outer():
	print("This is outer function")
	def inner():
		print("This is inner function")

>>> name = "Ram"
>>> def outer():
	print(name)
	print("This is outer function")
	def inner():
		print(name)
		print("This is inner function")

		
>>> def outer():
	name_1 = "Ram"
	print(name_1)
	print("This is outer function")
	def inner():
		print(name_1)
		print("This is inner function")

		
>>> outer()
Ram
This is outer function
>>> name
'Ram'
>>> name_1
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    name_1
NameError: name 'name_1' is not defined
>>> def outer():
	name_1 = "Ram"
	print(name_1)
	print("This is outer function")
	def inner():
		print(name_1)
		print("This is inner function")
	inner()

	
>>> outer()
Ram
This is outer function
Ram
This is inner function
>>> 
