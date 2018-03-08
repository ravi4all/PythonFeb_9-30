import csv

# Data = [
#     {'Name':'Ram','Email':'ram@gmail.com','pwd':'12345'},
#     {'Name':'Ramesh','Email':'ramesh@gmail.com','pwd':'45678'},
#     {'Name':'Raman','Email':'raman@gmail.com','pwd':'abcde'}
# ]

def saveData(data):
    try:
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            # writer.writerow(data.values())

            for d in data:
                writer.writerow(d.values())
                # for d1 in d.values():
                #     print(d1)
    except FileNotFoundError:
        print("File not found")

# saveData(Data)

def readData():
    data = []
    try:
        with open('data.csv') as file:
            reader = csv.reader(file)
            for rows in reader:
                data.append(rows)
    except FileNotFoundError:
        print("File Not Found")

    return data

# d = readData()
# for i in d:
#     print(i)