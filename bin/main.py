# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from aslib import csv2dict_reader

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Start!')
    path = "/home/keith/Projects/Python/AS_Counts_Stats_Commission/data/single.csv"
    load_csv = csv2dict_reader.csv2dict(path)
    print(load_csv)
    print("Done!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
