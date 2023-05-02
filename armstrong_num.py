"""
Python Program to check Armstrong Number
Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
"""
def check_armstrong_num(num1):
    result=0
    for i in num1:
        result=result+int(i)**len(num1)
    
    return "{} is Armstrong Number".format(num1) if (result==int(num1)) else "{} Not Armstrong Number".format(num1)
    

number1=input('Provide your Number: ')
check_armstrong_num(number1)

"""
OUTPUT
Provide your Number: 10
'10 Not Armstrong Number

Provide your Number: 120
'120 Not Armstrong Number'

Provide your Number: 1634
'1634 is Armstrong Number'

Provide your Number: 120
'120 Not Armstrong Number'

"""