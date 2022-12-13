# This is a sample Python script.

import csv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def csv2dict(path):
    keys = []
    values = []
    with open(path, 'r') as csvfile:
        csvreader = csv.reader(csvfile) #Obj to read file
        keys = next(csvreader)
        # print(keys)

        # Fetch the values
        for row in csvreader:
            values.append(row)
        # print(values)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Keith')
    path = "/home/keith/Projects/Python/AS_Counts/data/single.csv"
    csv2dict(path)
    print("Done!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
