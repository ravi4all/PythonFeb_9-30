Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "Hello Python"
>>> a[0]
'H'
>>> a[5]
' '
>>> a[0:5]
'Hello'
>>> a[0:]
'Hello Python'
>>> a[:10]
'Hello Pyth'
>>> a[:]
'Hello Python'
>>> a[:100]
'Hello Python'
>>> a[0:10:2]
'HloPt'
>>> a[-1]
'n'
>>> a[-2]
'o'
>>> a[::-1]
'nohtyP olleH'
>>> str_1 = "Python"
>>> str_2 = str_1[::-1]
>>> str_2
'nohtyP'
>>> str_1 == str_2
False
>>> str_1 = "nitin"
>>> str_2 = str_1[::-1]
>>> str_1 == str_2
True
>>> str_1 is str_2
False
>>> str_3 = str_1
>>> str_1 is str_3
True
>>> 
