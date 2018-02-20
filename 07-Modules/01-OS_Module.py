Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Python36'
>>> os.chdir('C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\Feb_2018\Python_Morning_9-30')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir(r'C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\Feb_2018\Python_Morning_9-30')
>>> os.getcwd()
'C:\\Users\\asus\\Documents\\Data\\DataTransfer\\BMPL_Batches\\Feb_2018\\Python_Morning_9-30'
>>> os.chdir('04-IfElse')
>>> os.startfile('PrimeNumber.py')
>>> os.chdir(r'C:\Python36')
>>> os.startfile('dhoni.mp4')
>>> os.startfile('music_2.ogg')
>>> os.system('notepad')
0
>>> os.system('calc')
0
>>> 
