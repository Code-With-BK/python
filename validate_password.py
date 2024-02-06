"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2024. All rights reserved.
 
 Python program to validate a password string

 A password is valid if
 a) It is between 6-20 characters
 b) It contains at least one upper case letter
 c) It contains at least one lower case letter
 d) It contains at least one digit
 e) It contains at least one special character

"""

def is_valid_password(s):
    # a) between 6-20 characters
    l = len(s)
    if( l<6 or l>20 ):
        return False 
    
    # b), c), d), e)
    contains_upper_case = False
    contains_lower_case = False
    contains_digit = False
    contains_special_char = False

    for i in range(l):
        ch = s[i]
        # check if ch is upper case
        if( ch.isupper() ):
            contains_upper_case = True
        # check if ch is lower case
        if( ch.islower() ):
            contains_lower_case = True 
        # check if ch is digit
        if( ch.isdigit() ):
            contains_digit = True 
        # check if ch is special char
        if( not ch.isdigit() and not ch.isalpha() and not ch.isspace() ):
            contains_special_char = True 

    # return value
    return contains_upper_case and contains_lower_case and contains_digit and contains_special_char

def main():
    f = open("passwords.txt", "r")
    lines = f.readlines() 
    f.close() 

    # remove '\n' from the end of each string
    for i in range(len(lines)):
        line = lines[i] 
        line = line[:-1]
        lines[i] = line 
    
    for line in lines:
        if( is_valid_password(line) ):
            print(f"Is {line} a valid password? YES")
        else:
            print(f"Is {line} a valid password? NO")
            
main()
