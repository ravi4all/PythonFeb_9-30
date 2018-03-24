# *args
# **kwargs

def emp(id,name,salary,*address):
    print("ID : {}".format(id))
    print("Name : {}".format(name))
    print("Salary : {}".format(salary))
    # print("Address : {}".format(address))
    for i in range(len(address)):
        print("Address : {} - {}".format(i+1,address[i]))

# emp(101,'Ram',12000,'Rohini')
# emp(101,'Ram',12000,['Rohini','Rithala'])

# emp(101,'Ram',25000,'Rohini','Rithala','Saket')

def student(**details):
    print("Details",details)

student(name='Ram',age=19,college='IP',gender='M')
student(name='Shyam',college='DU',gender='M')
student(name='Pooja',college='IP')