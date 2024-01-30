"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2024. All rights reserved.
 
 Python program to print the lucky numbers less than n
 1 < n < 100000

 Example 1: 
 n = 25
 Output:
 1 3 7 9 13 15 21 

 Example 2:
 n = 100
 Output:
 1 3 7 9 13 15 21 25 31 33 37 43 49 51 63 67 69 73 75 79 87 93 99


 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
 1   3   5   7   9    11    13    15    17    19    21    23   
 1   3       7   9          13    15          19    21 
 1   3       7   9          13    15                21 

"""

# print all the lucky numbers less than n
def lucky_numbers(n):

    lucky_numbers = [0] * n
    # ith index has value i
    for i in range(n):
        lucky_numbers[i] = i 
    
    # index 0 is redundant
        
    # remove all even numbers
    for i in range(n):
        if( i%2==0 ):
            lucky_numbers[i] = 0 
    # print(lucky_numbers)
    
    # remove the remaining set of values
    j = 3 # remove every jth value
    while( j<n ):
        # remove every jth non-zero value from the list
        m = 1       # m will cover all indices which are non-zero
        while( m<n ):
            count = 0
            while( m<n ):
                if( lucky_numbers[m]!=0 ):
                    count += 1 
                if( count==j ):
                    break 
                m += 1
            if( count==j ):
                lucky_numbers[m] = 0
        # print(lucky_numbers)
            
        # find the next j
        m = j + 1
        while( m<n and lucky_numbers[m]==0 ):
            m += 1
        j = m
            
    # print the lucky numbers
    print(f"Lucky numbers less than {n} are: ", end="")
    for i in range(n):
        if( lucky_numbers[i] != 0 ):
            print(lucky_numbers[i], end = " ")
    print()

def main():
    n = 10
    lucky_numbers(n)

# run the main
main()
