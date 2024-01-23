"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2024. All rights reserved.
 
 Python program to right rotate list elements n times
  
 Example 1:
 Input:
 integers = [7, 10, 11, 18, 97]
 n = 1
 Output:
 [97, 7, 10, 11, 18]

 Example 2:
 Input:
 integers = [7, 10, 11, 18, 97]
 n = 3
 Output:
 [11, 18, 97, 7, 10]

 [7, 10, 11, 18, 97]
 [7, 10, 11, 18, 18]
 [7, 10, 11, 11, 18]
 [7, 10, 10, 11, 18]
 [7, 7, 10, 11, 18]
 [97, 7, 10, 11, 18]
"""
from collections import deque

# rotate list elements right ONCE, IN PLACE
def rotate_right1(integers):
    l = len(integers)
    temp = integers[l-1]
    i = l-1
    while( i>0 ):
        integers[i] = integers[i-1]
        i -= 1
    integers[0] = temp 

# rotate list elements right N TIMES, IN PLACE
def rotate_right_n_times1(integers, n):
    for i in range(n):
        rotate_right1(integers)

# rotate list elements right ONCE, creates a NEW LIST
def rotate_right2(integers):
    l = len(integers)
    rotated_integers = [0]*l 
    for i in range(l):
        new_i = (i+1)%l
        rotated_integers[new_i] = integers[i]
    return rotated_integers

# rotate list elements right N TIMES, creates a NEW LIST
def rotate_right_n_times2(integers, n):
    l = len(integers)
    rotated_integers = [0]*l 
    for i in range(l):
        new_i = (i+n)%l
        rotated_integers[new_i] = integers[i]
    return rotated_integers

# rotate list elements right ONCE, creates a NEW LIST
def rotate_right3(integers):
    #  0  1   2   3   4
    # [7, 10, 11, 18, 97]
    # 
    # -5  -4  -3  -2  -1
    # [7, 10, 11, 18, 97]
    #
    #
    #
    l = len(integers)
    rotated_integers = integers[-1:l] + integers[0:-1]
    return rotated_integers

# rotate list elements right N TIMES, creates a NEW LIST
def rotate_right_n_times3(integers, n):
    #  0  1   2   3   4
    # [7, 10, 11, 18, 97]
    # 
    # -5  -4  -3  -2  -1
    # [7, 10, 11, 18, 97]
    #
    #
    #
    l = len(integers)
    if( n>l ):
        n = n%l
    rotated_integers = integers[-n:l] + integers[0:-n]
    return rotated_integers

# rotate list elements right ONCE, creates a NEW LIST
def rotate_right4(integers):
    #  0  1   2   3   4
    # [7, 10, 11, 18, 97]
    # 
    # -5  -4  -3  -2  -1
    # [7, 10, 11, 18, 97]
    #
    #
    #
    deq1 = deque(integers)
    deq1.rotate(1)
    rotated_integers = list(deq1)
    return rotated_integers

# rotate list elements right N TIMES, creates a NEW LIST
def rotate_right_n_times4(integers, n):
    #  0  1   2   3   4
    # [7, 10, 11, 18, 97]
    # 
    # -5  -4  -3  -2  -1
    # [7, 10, 11, 18, 97]
    #
    #
    #
    deq1 = deque(integers)
    deq1.rotate(n)
    rotated_integers = list(deq1)
    return rotated_integers

def main():
    integers = [7, 10, 11, 18, 97]
    n = 11
    print(integers)
    # rotate_right1(integers)
    # rotate_right_n_times1(integers, n)
    # print(integers)
    # rotated_integers = rotate_right2(integers)
    # rotated_integers = rotate_right_n_times2(integers, n)
    # rotated_integers = rotate_right3(integers)
    # rotated_integers = rotate_right_n_times3(integers, n)
    # rotated_integers = rotate_right4(integers)
    rotated_integers = rotate_right_n_times4(integers, n)
    print(rotated_integers)
    # print(integers)

main()
