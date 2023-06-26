"""
Python Program for How to check if a given number is Fibonacci number?

A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square

1, 1, 2, 3, 5, 8, 13, 21

perfect Square:A perfect square is a positive integer that is obtained by multiplying an integer by itself. 
"""
import math
def check_if_fibonacci(n):
    
    result=[]
    result.append(int(math.sqrt((5*(n*n)+4))))
    result.append(int(math.sqrt((5*(n*n)-4))))
    
    for i in result:
        
        if ((i*i)==(5*(n*n)+4)) or ((i*i)==(5*(n*n)-4)):
            
            return "{} is a fibonacci number: ".format(n)
            break
    else:
        return "{} is not a fibonacci number: ".format(n)
 

number1=int(input("Provide your input nth position: "))

check_if_fibonacci(number1)

"""
#OUTPUT

Provide your input nth position: 1
'1 is a fibonacci number: '

Provide your input nth position: 2
'2 is a fibonacci number: '

Provide your input nth position: 3
'3 is a fibonacci number: '
​
Provide your input nth position: 4
'4 is not a fibonacci number: '

Provide your input nth position: 5
'5 is a fibonacci number: '
"""