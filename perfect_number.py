
"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.
 
 Python program to check whether a number is a perfect number 

 - a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. 
 - For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number
"""

# n = 100
# divisors_sum = 0
# for i in range(1,n):
#     if( n%i==0 ):
#         divisors_sum += i 
# if( divisors_sum==n ):
#     print(f"{n} is a Perfect Number")
# else:
#     print(f"{n} is not a Perfect Number")

divisors = []
def perfect_number(n):
    divisors.clear()
    divisors_sum = 0
    for i in range(1,n):
        if( n%i==0 ):
            divisors_sum += i 
            divisors.append(i)
    if( divisors_sum==n ):
        # print(f"{n} is a Perfect Number")
        return True
    else:
        # print(f"{n} is not a Perfect Number")
        return False
    
def main():
    for i in range(1,10000):
        if( perfect_number(i) ):
            print(f"{i} is a Perfect Number")
            print(f"Divisors of {i}: {divisors}")
            print()

main()

