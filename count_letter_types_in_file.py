
"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.
 
 Python program to read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file
"""
def count_letter_types(filename):
    num_vowels = 0
    num_consonants = 0
    num_uppercase = 0
    num_lowercase = 0
    num_whitespaces = 0
    f_in = open(filename)
    lines = f_in.readlines()
    f_in.close()

    for line in lines:
        # remove the last newline character
        line = line[:-1]
        # pickup each character in this line
        for ch in line:
            # if this is a vowel
            vowels = "aeiouAEIOU"
            if( ch in vowels ):
                num_vowels += 1
            # if this is a consonant
            if( ch.isalpha() and ch not in vowels ):
                num_consonants += 1
            # if this is an uppercase letter
            if( ch.isupper() ):
                num_uppercase += 1
            # if this is a lowercase letter
            if( ch.islower() ):
                num_lowercase += 1
            # if this character is a whitespace
            if( ch.isspace() ):
                num_whitespaces += 1

    print(f"Number of vowels: {num_vowels}")
    print(f"Number of consonants: {num_consonants}")
    print(f"Number of uppercase letters: {num_uppercase}")
    print(f"Number of lowercase letters: {num_lowercase}")
    print(f"Number of whitespaces: {num_whitespaces}")

def main():
    filename = "in3.txt"  
    count_letter_types(filename)

main()
