# Method to read CSV files and return data in a list
import csv


def read_csv(file_to_read: str):
    data = []
    with open(file_to_read, newline='') as csv_file:
        new_reader = csv.reader(csv_file)
        for row in new_reader:
            data.append(row)
    return data
