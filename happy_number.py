"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2024. All rights reserved. 

 Python program to check if an integer is a Happy Number or not

 A Happy Number is a number which eventually reaches 1 when 
 replaced by the sum of the square of each digit

 Example 1:
 n = 10
 Output:
 YES
 Explanation:
 10 = 1^2 + 0^2 = 1 + 0 = 1

 Example 2:
 n = 7
 Output:
 YES
 Explanation:
 7 = 7^2 = 49 
 = 4^2 + 9^2 = 16 + 81 = 97 
 = 9^2 + 7^2 = 81 + 49 = 130
 = 1^2 + 3^2 + 0^2 = 1 + 9 = 10 
 = 1^2 + 0^2 = 1 + 0 = 1
"""

def print_cycle():
    n = 4
    print("4", end="")
    start_n = n
    square_sum = 0
    while( square_sum!=start_n ):
        n_str = str(n)
        square_sum = 0
        for digit_ch in n_str:
            digit = int(digit_ch)
            digit_square = digit**2 
            square_sum += digit_square
        print(f"->{square_sum}")
        n = square_sum
    print()

def happy_number(n):
    if( n==1 ):
        return True 

    is_happy_num = False
    start_n = n
    while( True ):
        n_str = str(n)
        square_sum = 0
        for digit_ch in n_str:
            digit = int(digit_ch)
            digit_square = digit**2 
            square_sum += digit_square
        if( square_sum==1 ):
            is_happy_num = True 
            break 
        elif( square_sum==4 or square_sum==start_n ):
            is_happy_num = False 
            break
        else:
            n = square_sum
    return is_happy_num 

def main():
    # n = 4
    # print(f"{n} is a Happy Number? {happy_number(n)}")
    for i in range(1,101):
        if( happy_number(i) ):
             print(f"{i} is a Happy Number!")

# main()
print_cycle()