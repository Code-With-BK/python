"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.
 
 Python program to implement a stack using a list
"""

# Stack - uses LIFO - Last In First Out
# Push operation 
# Pop operation 

# Using list as a stack - considering right end as the stack top
# [] -> Top
# Push 10: [10] -> Top
# Push 20: [10, 20] -> Top
# Push 30: [10, 20, 30] -> Top
# Pop (removed 30 from the top): [10,20] -> Top
# Push operation : add element to the right end of the list
# Pop operation : remove element from the right end of the list

def push(integer_stack, element):
    # considering right end of the list as the top of the stack - add element to the right end of the list
    # integer_stack.append(element)
  
    # considering left end of the list as the top of the stack - add element to the left end of the list
    integer_stack.insert(0,element)


def pop(integer_stack):
    # return none if the stack is empty (that is the length of the list is 0)
    if( len(integer_stack)==0 ):
        return None
      
    # uncomment this line if the stack top if the right end of the list
    # popped_element = integer_stack.pop()

    # pop an element when stack top is the left end of the list
    popped_element = integer_stack.pop(0)
    return popped_element

def print_stack(integer_stack):
    l = len(integer_stack)
    if( l==0 ):
        print("Stack is empty")
        return
    print("Top -> ",end="")

    # print the stack top and other stack elements when stack top is the right end of the list 
    # print(f"{integer_stack[l-1]}")
    # for i in range(l-2,-1,-1):
    #     print(f"       {integer_stack[i]}")

    # print the stack top and other stack elements when stack top is the left end of the list 
    print(f"{integer_stack[0]}")
    for i in range(1,l):
        print(f"       {integer_stack[i]}")
    

integer_stack = []
push(integer_stack,10)
push(integer_stack,20)
push(integer_stack,30)
print_stack(integer_stack)
push(integer_stack,40)
print_stack(integer_stack)
print(f"Pop: {pop(integer_stack)}")
print_stack(integer_stack)
print(f"Pop: {pop(integer_stack)}")
print_stack(integer_stack)
