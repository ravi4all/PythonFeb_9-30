import csv

data = [
    'First Name,Last Name'.split(','),
    'Sachin,Tendulkar'.split(","),
    'MS,Dhoni'.split(','),
    'Yuvraj,Singh'.split(','),
    'Ishant,Sharma'.split(',')
]

# data = [
#     ['First Name','Last Name'],
#     ['Sachin', 'Tendulkar']
# ]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for d in data:
        writer.writerow(d)