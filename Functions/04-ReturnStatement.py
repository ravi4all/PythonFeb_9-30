def calc(x,y):
    return x + y, x-y,x/y,x*y

def emp():
    empname = "Ram"
    print("Hello",empname)
    return empname

# a = calc(2,4)
# print(a)

# a,b,c,d = calc(12,4)
# print(a,b,c,d)

a,*b = calc(12,4)       # Unpacking values
print(a,b)

emp()