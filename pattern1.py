
"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.
 
 Python program to print the following pattern
 *
 **
 ***
 ****
 *****
"""

def print_pattern1(n):
    for i in range(1,n+1):
        print("*"*i)

print_pattern1(5)