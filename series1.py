"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.
 
 Python program to input the value of x and n and 
 print the sum of the following series:
 1 + x + x^2 + x^3 + x^4 + . . . x^n
"""

def calculate_series1(x,n):
    sum = 0
    for power in range(0, n+1):
        term = x**power 
        sum += term
    return sum 

def main():
    # 1 + 3 + 9 + 27 + 81 + 243
    x = 3
    n = 5
    series1 = calculate_series1(x,n)
    print(series1)

main()
