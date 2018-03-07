import csv

with open('data.csv') as file:
    reader = csv.reader(file)

    # print(reader)
    
    for data in reader:
        print(data)