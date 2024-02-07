"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2024. All rights reserved.
 
 Python program to remove all occurrences of a char x from a string s

 Example 1:
 s = "My name is Balkrishna"
 x = 'a'
 Output:
 "My nme is Blkrishn"

 Example 1:
 s = "Python in Hindi"
 x = 'i'
 Output:
 "Python n Hnd"

"""

def remove_all_chars1(s, x):
    new_string = ""
    for ch in s:
    # for i in range(len(s)):
        # ch = s[i]
        if( ch!=x ):
            new_string += ch 
    return new_string 

# replace() method
def remove_all_chars2(s, x):
    new_string = s.replace(x, "")
    return new_string

# join() method
def remove_all_chars3(s, x):
    new_string = "".join(ch for ch in s if ch!=x )
    return new_string

def main():
    s = "Python in Hindi"
    # s = "My name is Balkrishna"
    x = 'i'
    # x = 'a'
    # s_ = remove_all_chars1(s ,x)
    # s_ = remove_all_chars2(s ,x)
    s_ = remove_all_chars3(s ,x)
    print(s_)

main()
