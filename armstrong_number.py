
"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.
 
 Python program to check whether a number is an Armstrong Number 

 - a number n is an Armstrong Number if the sum of its own digits raised to the power number of digits gives the number itself
 - For instance, n=153 has 3 digits: 1, 5, 3, and 
   1^3=1
   5^3=125
   3^3=27
   and, 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 (equal to n)
   So, 153 is an Armstrong Number
 - 1634 is an Armstrong Number too 
   1^4=1
   6^4=1296
   3^4=81
   4^4=256
   and, 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634 (equal to 1634)
"""


# check if n is an armstrong number - using strings
def armstrong_number1(n):
  n_str = str(n) 
  num_digits = len(n_str)
  sum = 0
  for digit_str in n_str:
      digit = int(digit_str)
      term = digit**num_digits
      sum += term
  if( sum==n ):
      return True
  else:
      return False
  
# check if n is an armstrong number - using loops
def armstrong_number2(n):
  num_digits = 0
  temp = n
  while( n!=0 ):
      num_digits += 1
      n = n//10
  n = temp
  sum = 0
  while( n!=0 ):
      digit = n%10
      n = n//10
      term = digit**num_digits
      sum += term
  n = temp 
  if( n==sum ):
      return True 
  else:
      return False
  
def main():
    for i in range(1,100000):
        # if( armstrong_number1(i) ):
        #     print(f"{i} is an Armstrong Number")
        if( armstrong_number2(i) ):
            print(f"{i} is an Armstrong Number")
        if( armstrong_number2(i) != armstrong_number1(i) ):
            print(f"{i} : Error")

main()  



