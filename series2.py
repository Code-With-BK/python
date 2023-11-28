"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.
 
 Python program to input the value of x and n and 
 print the sum of the following series:
 1 - x + x^2 - x^3 + x^4 - . . . xn
"""

def calculate_series2(x,n):
    sum = 0
    for power in range(0, n+1):
        term = x**power 
        if( power%2==0 ):
            sum += term
        else:
            sum -= term
    return sum 

def main():
    # 1 - 2 + 4 - 8 + 16 - 32
    x = 2
    n = 5
    series2 = calculate_series2(x,n)
    print(series2)

main()


