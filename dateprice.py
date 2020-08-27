#!/usr/bin/python3
import csv

with open("test-data/account.csv") as account_file:
    d_reader = csv.DictReader(account_file)
    headers = d_reader.fieldnames
    for line in d_reader:
        for header in headers:
            print(f"{line[header]} ", end='')

if __name__ == '__main__':
    print("hello danny")
