
import csv

def csv2dict(path):
    print("Opening CSV file...")
    keys = []
    values = []
    with open(path, 'r') as csvfile:
        csvreader = csv.reader(csvfile) #Obj to read file
        keys = next(csvreader)
        print(keys)

        # Fetch the values
        for row in csvreader:
            values.append(row)
        print(values)
    return 7
