
"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.
 
 Python program to print the following pattern
 A
 AB
 ABC
 ABCD
 ABCDE
"""

def print_pattern3(n):
    for i in range(n):
        for j in range(i+1):
            char = chr(ord('A')+j)
            print(char,end="")
        print()
        
print_pattern3(5)