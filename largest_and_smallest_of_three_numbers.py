"""
@author Balkrishna Srivastava
Copyright © CodeWithBK 2023. All rights reserved.

Python program to input three numbers and display the largest and smallest number using i) if-else ii) list & sorting
"""

input1 = input("Enter a number: ")
input2 = input("Enter another number: ")
input3 = input("Enter a third number: ")

# if the expected input type is int
# a = int(input1)
# b = int(input2)
# c = int(input3)

# if the expected input type is float
a = float(input1)
b = float(input2)
c = float(input3)

# 1. use if-else
print("Using if-else...")

# find the largest first
# if a>b 
if (a>b):
    if (a>c):
        # if a>b and if a>c => a is the largest
        print("Largest:",a)
    else:
        # if a>b and if a<c => b<a<c => c is the largest
        print("Largest:",c)
# if a<b
else:
    if(b<c):
        # if a<b and if b<c => a<b<c => c is the largest
        print("Largest:",c)
    else:
        # if a<b and b>c => b is the largest
        print("Largest:",b)


# find the smallest 
# if a<b
if( a<b ):
    if( a<c ):
        # if a<b and if a<c => a is the smallest
        print("Smallest:",a)
    else:
        # if a<b and a>c => c<a<b => c is the smallest
        print("Smallest:",c)
else:
    # if b<a
    if( b<c ):
        # if b<a and if b<c => b is the smallest
        print("Smallest:",b)
    else:
        # if b<a and b>c => c<b<a => c is the smallest
        print("Smallest:",c)


# 2. use list and sorting
print()
print("Using sorting...")
numbers = []
numbers.append(a)
numbers.append(b)
numbers.append(c)
numbers.sort()
print("Largest:",numbers[2])
print("Smallest:",numbers[0])

