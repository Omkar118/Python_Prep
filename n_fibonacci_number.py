"""
Python Program for n-th Fibonacci number

1, 1, 2, 3, 5, 8, 13, 21

Fn = Fn-1 + Fn-2
"""

def find_fibonacci_number(n):
    
    if n<= 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
        # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return find_fibonacci_number(n-1)+find_fibonacci_number(n-2)
    pass
 

number1=int(input("Provide your input nth position: "))

find_fibonacci_number(number1)

"""
OUTPUT

Provide your input nth position: 10
34

Provide your input nth position: 2
1
"""