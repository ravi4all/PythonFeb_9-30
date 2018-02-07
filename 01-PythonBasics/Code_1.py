Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 12
>>> b = 15
>>> a+b
27
>>> a-b
-3
>>> import keywords
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    import keywords
ModuleNotFoundError: No module named 'keywords'
>>> import keyword
>>> print("Hello")
Hello
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a = "Hello"
>>> type(a)
<class 'str'>
>>> type(str)
<class 'type'>
>>> type(type)
<class 'type'>
>>> a = "Hello "World""
SyntaxError: invalid syntax
>>> a = "Hello \"World""
SyntaxError: EOL while scanning string literal
>>> a = "Hello \"World\""
>>> a
'Hello "World"'
>>> print(a)
Hello "World"
>>> a = 'Hello "World"'
>>> print(a)
Hello "World"
>>> a = 'Hello\nWorld'
>>> print(a)
Hello
World
>>> a = r'Hello\nWorld'
>>> print(a)
Hello\nWorld
>>> path = 'C:\Python36\Lib\site-packages'
>>> path = 'C:\Python36\nic\site-packages\asus'
>>> print(path)
C:\Python36
ic\site-packagessus
>>> path = 'C:/Python36/nic/site-packages/asus'
>>> path = r'C:\Python36\nic\site-packages\asus'
>>> 
