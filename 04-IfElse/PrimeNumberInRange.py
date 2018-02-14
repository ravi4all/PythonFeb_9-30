import time

min_range = int(input("Enter min range : "))
max_range = int(input("Enter max range : "))

start_time = time.time()
for num in range(min_range, max_range):
    for i in range(2,num):
        if num % i == 0:
            #print("{} is not Prime number".format(num))
            break
    else:
        pass
        #print("{} is a Prime number".format(num))

#print("Script started at",start_time)
end_time = time.time()
total_time = end_time - start_time
print("Total Time",total_time)
