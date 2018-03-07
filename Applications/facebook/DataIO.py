import csv

# Data = [
#     {'Name':'Ram','Email':'ram@gmail.com','pwd':'12345'},
#     {'Name':'Ramesh','Email':'ramesh@gmail.com','pwd':'45678'},
#     {'Name':'Raman','Email':'raman@gmail.com','pwd':'abcde'}
# ]

def saveData(data):
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # writer.writerow(data.values())

        for d in data:
            writer.writerow(d.values())
            # for d1 in d.values():
            #     print(d1)

# saveData(Data)