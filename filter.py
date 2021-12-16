import csv

data = []

with open('final.csv') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers = data[0]
planets_data = data[1:]

new_data = []

for index , row in enumerate(planets_data):
    if(row[2]!=''):
        if float(row[2]) < 100 and float(row[2]) > 0:
            new_data.append(row)
    
print(new_data)