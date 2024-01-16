"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2024. All rights reserved. 

 Python program to check if an integer is a Disarium Number or not

 A number is called Disarium if sum of its digits powered with their 
 respective positions is equal to the number itself

 Example 1:
 n = 135
 Output:
 YES
 Explanation:
 135 -> 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

 Example 2:
 n = 89
 Output:
 YES
 Explanation:
 89 = 8^1 + 9^2 = 8 + 81 = 89
"""

def disarium_number(n):
    sum = 0
    n_str = str(n)
    power = 1
    for digit_ch in n_str:
        digit = int(digit_ch)
        sum += digit**power 
        power += 1
    return sum==n 

def main():
    # n = 8
    # print(f"Is {n} a disarium number? {disarium_number(n)}")
    for i in range(1,10001):
        if( disarium_number(i) ):
            print(f"{i} is a disarium number!")

main()