#!/usr/bin/python3

import csv

def filters_csv(csv_file_path):
    with open(csv_file_path, "r", newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['Name'].startswith('G'):
                print(row)

csv_file_path = 'data.csv'
filters_csv(csv_file_path)

