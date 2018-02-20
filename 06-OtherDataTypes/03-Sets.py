Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = [2,3,45,7,8,9,6,6,4,2,1,3,7]
>>> unique_x = set(x)
>>> unique_x
{1, 2, 3, 4, 6, 7, 8, 9, 45}
>>> unique_x[4]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    unique_x[4]
TypeError: 'set' object does not support indexing
>>> set_1 = {1, 2, 3, 4, 6, 7, 8, 9, 45}
>>> set_2 = {2, 3, 6, 9, 5, 8, 12, 19, 4}
>>> len(set_1)
9
>>> len(set_2)
9
>>> set_1 & set_2
{2, 3, 4, 6, 8, 9}
>>> set_1 | set_2
{1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 45, 19}
>>> set_1.union(set_2)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 45, 19}
>>> str_1 = "Hello world, this is python programming and python is used for machine learning"
>>> str_2 = "Python is basically a general purpose programming and also used for machine learning"
>>> str_1 = str_1.lower()
>>> str_2 = str_2.lower()
>>> str_1
'hello world, this is python programming and python is used for machine learning'
>>> str_2
'python is basically a general purpose programming and also used for machine learning'
>>> token_1 = str_1.split()
>>> toke_1
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    toke_1
NameError: name 'toke_1' is not defined
>>> token_1
['hello', 'world,', 'this', 'is', 'python', 'programming', 'and', 'python', 'is', 'used', 'for', 'machine', 'learning']
>>> token_2 = str_2.split()
>>> token_2
['python', 'is', 'basically', 'a', 'general', 'purpose', 'programming', 'and', 'also', 'used', 'for', 'machine', 'learning']
>>> stopwords = ['and','is','for','this','a','b','that','also']
>>> wordlist_1 = []
>>> for word in token_1:
	if word not in stopwords:
		wordlist_1.append(word)

		
>>> wordlist_1
['hello', 'world,', 'python', 'programming', 'python', 'used', 'machine', 'learning']
>>> wordlist_2 = []
>>> for word in token_2:
	if word not in stopwords:
		wordlist_2.append(word)

		
>>> wordlist_2
['python', 'basically', 'general', 'purpose', 'programming', 'used', 'machine', 'learning']
>>> set_1 = set(wordlist_1)
>>> set_1
{'machine', 'used', 'hello', 'python', 'programming', 'world,', 'learning'}
>>> set_2 = set(wordlist_2)
>>> set_2
{'basically', 'purpose', 'machine', 'general', 'used', 'python', 'programming', 'learning'}
>>> len(set_1 & set_2) / len(set_1 | set_2)
0.5
>>> 
