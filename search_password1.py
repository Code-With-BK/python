"""
@author Balkrishna Srivastava
Copyright © CodeWithBK 2023. All rights reserved.

Python program to read a csv file containing usernames and passwords
Search the password for given input username

Without using the csv module
"""

search_username = input("Enter a username to search: ")

filename = "passwords.csv"
found = False
f = open(filename, 'r')
lines = f.readlines()
lines.pop(0) # remove the header row
# print(lines)
for line in lines:
    # print(line, end="")
    row_items = line.split(",")
    # print(row_items)
    username = row_items[0]
    password = row_items[1]
    password = password[:-1]
    # print(f"Username '{username}' has password '{password}'")
    if( search_username==username ):
        print(f"Username '{username}' has password '{password}'")
        found = True
f.close()
if( not found ):
    print(f"Username '{search_username}' does not exist!")