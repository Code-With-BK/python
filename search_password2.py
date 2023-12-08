"""
@author Balkrishna Srivastava
Copyright © CodeWithBK 2023. All rights reserved.

Python program to read a csv file containing usernames and passwords
Search the password for given input username

Using the csv module
"""
import csv

search_username = input("Enter a username to search: ")
filename = "passwords.csv"
found = False
f = open(filename, 'r')
csvreader = csv.reader(f)
rows = list(csvreader)
# for row in csvreader:
rows.pop(0)
# print(rows)
for row in rows:
    # print(row)
    username = row[0]
    password = row[1]
    if( search_username==username ):
        print(f"Username '{username}' has password '{password}'")
        found = True
f.close()
if( not found ):
    print(f"Username '{search_username}' does not exist!")

