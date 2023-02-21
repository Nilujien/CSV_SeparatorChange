# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import pathlib
from pathlib import Path



def change_csv_separator():

    path = "C:/Users/JCUARTERO/Documents/CSV_SampleTestFile.csv"

    reader = list(csv.reader(open(path, "r"), delimiter=','))
    writer = csv.writer(open(path, 'w'), delimiter=';')
    writer.writerows(row for row in reader)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    change_csv_separator()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
