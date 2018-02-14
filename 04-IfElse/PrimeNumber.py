# Prime Numbers
# 1,3,5,7,11,13,17

num = int(input("Enter the number : "))

for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("{} is a Prime Number".format(num))
