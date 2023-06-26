"""
Python Program for Sum of squares of first n natural numbers

Input : N = 4
Output : 30
12 + 22 + 32 + 42
= 1 + 4 + 9 + 16
= 30

Input : N = 5
Output : 55
"""

def natural_num_sqr(num1):
    result=0
    for i in range (1,num1+1):
        result=result+(i**2)
        
    return result

input_num=int(input("Enter the number to calculate square of first n natural numbers: "))
print("Sum of Squares of first ",input_num,"natural numbers is:",natural_num_sqr(input_num))

"""
OUTPUT
Enter the number to calculate square of first n natural numbers: 4
Sum of Squares of first  4 natural numbers is: 30

Enter the number to calculate square of first n natural numbers: 5
Sum of Squares of first  5 natural numbers is: 55

"""