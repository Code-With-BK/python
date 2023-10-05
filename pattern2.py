
"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.
 
 Python program to print the following pattern
 12345
 1234
 123
 12
 1
"""

def print_pattern2(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end="")
        print()
        
print_pattern2(5)

