"""
Python Program to Check Prime Number
"""

def check_prime_func(num1):
    if num1==0 or num1==1:
        result="{} is not a prime number".format(num1)
        
    else:
        
        for i in range (2,(int(num1/2)+1)):
            if num1%i==0:
                result="{} is not prime as it is divisible by {},etc".format(num1,i)
                break;

        else:
            result="{} is prime number".format(num1)
        
    return result

number1=int(input("Provide your input: "))

check_prime_func(number1)

"""
OUTPUT

Provide your input: 127
'127 is prime number'
​
Provide your input: 3
'3 is prime number'

Provide your input: 54
'54 is not prime as it is divisible by 2,etc'

Provide your input: 7
'7 is prime number'
"""