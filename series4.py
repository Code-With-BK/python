"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.
 
 Python program to input the value of x and n and 
 print the sum of the following series:
 x + x^2/2! + x^3/3! + x^4/4! + . . . x^n/n!
"""

def factorial(n):
    # n! = 1 x 2 x 3 x 4 .... n
    product = 1
    for i in range(1,n+1):
        product *= i 
    return product

def calculate_series4(x,n):
    sum = 0
    for power in range(1,n+1):
        power_fact = factorial(power)
        term = (x**power)/power_fact
        sum += term 
    return sum

def main():
    # 2 + (4/2) + (8/6) + (16/24)
    # 2 + 2 + 1.33 + 0.66
    # 4 + ~2
    # 6 
    x = 2
    n = 4
    series4 = calculate_series4(x,n)
    print(series4)

main()
