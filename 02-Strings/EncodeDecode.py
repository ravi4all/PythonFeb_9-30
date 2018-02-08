Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Feb_2018/Python_Morning_9-30/02-Strings/01-StringsMethods.py 
Enter first name : ram
Enter last name : sharma
                                                                       Welcome                                                                        
Hello ram sharma
Hello Virat Kohli
Hello b'ram'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Feb_2018/Python_Morning_9-30/02-Strings/01-StringsMethods.py 
Enter first name : राम
Enter last name : शर्मा
कृपया अपना पता डाले : क्स्य्ज़
                                                                       Welcome                                                                        
Hello राम शर्मा
Hello Virat Kohli
हेल्लो b'\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae'
>>> firstName
'राम'
>>> firstName.encode('UTF-8')
b'\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae'
>>> encodedName = firstName.encode('UTF-8')
>>> encodedName
b'\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae'
>>> encodedName.decode()
'राम'
>>> 
