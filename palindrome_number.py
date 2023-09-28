"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.
 
 Python program to check whether a number is a Palindrome

 - a number n is a palindrome it the reverse number of n is equal to n
 - For instance, n=34543 is a palindrome number, since reverse of 34543 = 34543

 - Using two approaches
 i) Using strings
 ii) Using while loops
"""

# n = 134431
# n_str = str(n)  # "34543"
# reverse_n = ""
# j = len(n_str) - 1
# while( j>=0 ):
#     reverse_n += n_str[j]
#     j -= 1
# if( n_str == reverse_n ):
#     print(f"{n} is a Palindrome")
# else:
#     print(f"{n} is not a Palindrome")

# check palindrome using string 
def palindrome1(n):
    n_str = str(n)  # "34543"
    reverse_n = ""
    j = len(n_str) - 1
    while( j>=0 ):
        reverse_n += n_str[j]
        j -= 1
    if( n_str == reverse_n ):
        return True
    else:
        return False

# find palindrome using while loops 
def palindrome2(n):
    reverse_n = 0
    temp = n 
    while( n!=0 ):
        digit = n%10
        reverse_n = reverse_n*10 + digit 
        n = n//10
    # reverse_n stores the reverse of n
    # n goes to 0
    n = temp
    if( n == reverse_n ):
        return True
    else:
        return False
    
def main():
    for i in range(1,100000):
        # if( palindrome1(i) ):
        #     print(f"{i} is a Palindrome")
        if( palindrome1(i) != palindrome2(i) ):
            print("Error")
main()