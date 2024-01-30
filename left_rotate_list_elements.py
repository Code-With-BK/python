"""
 @author Balkrishna Srivastava
 Copyleft © CodeWithBK 2024. All lefts reserved.
 
 Python program to left rotate list elements n times
  
 Example 1:
 Input:
 integers = [7, 10, 11, 18, 97]
 n = 1
 Output:
 [10, 11, 18, 97, 7]

 Example 2:
 Input:
 integers = [7, 10, 11, 18, 97]
 n = 3
 Output:
 [18, 97, 7, 10, 11]

 [7, 10, 11, 18, 97]
 [10, 11, 18, 97, 7]
 [11, 18, 97, 7, 10]
 [18, 97, 7, 10, 11]
"""

from collections import deque

# left rotate the list ONCE, IN PLACE
def left_rotate1(integers):
    l = len(integers)
    temp = integers[0]
    i = 0
    while( i<l-1 ):
        integers[i] = integers[i+1]
        i += 1
    integers[l-1] = temp

# left rotate the list N TIMES, IN PLACE
def left_rotate_n_times1(integers, n):
    for i in range(n):
        left_rotate1(integers)
       
# left rotate the list ONCE, create a NEW LIST
def left_rotate2(integers):
    l = len(integers)
    rotated_integers = [0] * l
    for i in range(l):
        new_i = i-1
        if( new_i<0 ):
            new_i += l 
        rotated_integers[new_i] = integers[i] 
    return rotated_integers

# left rotate the N TIMES, create a NEW LIST
def left_rotate_n_times2(integers,n):
    # negative indices
    #
    #  -5  -4 -3  -2  -1
    # [7, 10, 11, 18, 97]
    l = len(integers)
    rotated_integers = [0] * l
    for i in range(l):
        new_i = i-n
        while( new_i<0 ):
            new_i += l 
        rotated_integers[new_i] = integers[i] 
    return rotated_integers

# left rotate the list ONCE, create a NEW LIST
def left_rotate3(integers):
    l = len(integers)
    rotated_integers = integers[1:l] + integers[0:1]
    return rotated_integers

# left rotate the list N TIMES, create a NEW LIST
def left_rotate_n_times3(integers, n):
    l = len(integers)
    if( n>l ):
        n = n%l
    rotated_integers = integers[n:l] + integers[0:n]
    return rotated_integers

# left rotate the list ONCE, create a NEW LIST
def left_rotate4(integers):
    deq1 = deque(integers)
    deq1.rotate(-1)
    rotated_integers = list(deq1)
    return rotated_integers

# left rotate the list N TIMES, create a NEW LIST
def left_rotate_n_times4(integers, n):
    deq1 = deque(integers)
    deq1.rotate(-n)
    rotated_integers = list(deq1)
    return rotated_integers

def main():
    integers = [7, 10, 11, 18, 97]
    n = 13
    print(integers)
    # left_rotate1(integers)
    # left_rotate_n_times1(integers, n)
    # rotated_integers = left_rotate2(integers)
    # rotated_integers = left_rotate_n_times2(integers, n)
    # rotated_integers = left_rotate3(integers)
    # rotated_integers = left_rotate_n_times3(integers, n)
    # rotated_integers = left_rotate4(integers)
    rotated_integers = left_rotate_n_times4(integers, n)
    print(rotated_integers)
    # print(integers)

main()
