import csv

with open('test.csv', 'w') as csv_file:
    fieldnames = ['name','count']
    w = csv.DictWriter(csv_file, fieldnames)
    w.writeheader()
    w.writerow({'name': 'A', 'count':1})
    w.writerow({'name': 'B', 'count':2})
    
with open('test.csv', 'r') as csv_file:
    r = csv.DictReader(csv_file)
    for row in r:
        print(row['name'])
        print(row['count'])