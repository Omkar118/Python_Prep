"""
Program to print ASCII Value of a character

Given a character, we need to print its ASCII value in C/C++/Java/Python. 

Examples :

Input : a 
Output : 97

Input : D
Output : 68
"""

def print_ascii(chara_val):
    return ord(chara_val)

input_char=input("Enter Character to convert to ASCII: ")

print("ASCII Vaue of",input_char," is:",print_ascii(input_char))


"""
OUTPUT
Enter Character to convert to ASCII: a
ASCII Vaue of a  is: 97

Enter Character to convert to ASCII: A
ASCII Vaue of A  is: 65
"""