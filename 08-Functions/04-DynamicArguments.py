# Dynamic Arguments - *args and **kwargs

def emp(name,age,*address):
    print("Name : {}, age : {}".format(name,age))
    print("Address : {}".format(address))

emp("Ram",24,'Delhi', 'Noida', 'Agra', 'Pune')

def company(**details):
    print("Details :",details)

company(name='HCL',branch='Noida',teamSize=50)
company(name='TCS',branch='Pune')
