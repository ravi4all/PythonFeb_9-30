try:
    file = open('demo_1.txt')
    data = file.read()
    data_1 = "This data is written by python script"
    file.write(data_1)

except FileNotFoundError:
    print("File Not Found")
except BaseException:
    print("Some error occurred")

finally:
    print("I will always execute...")
    file.close()
    print("File closed successfully")

print("I also want to execute")