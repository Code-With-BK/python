"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.
 
 Python program to input the value of x and n and 
 print the sum of the following series:
 x + x^2/2 + x^3/3 + x^4/4 + . . . x^n/n
"""

def calculate_series3(x,n):
    sum = 0
    for power in range(1,n+1):
        term = (x**power)/power
        sum += term 
    return sum

def main():
    x = 2
    n = 4
    series3 = calculate_series3(x,n)
    print(series3)

main()