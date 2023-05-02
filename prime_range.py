"""
Python Program to Print all Prime numbers in an Interval
Given two positive integers start and end. 
The task is to write a Python program to print all Prime numbers in an Interval.
"""

def prime_num_printer(num1,num2):
    prime_list=[]
    for i in range (num1,num2):
        if i==0 or i==1:
            continue
        else:
            for j in range (2,(int(i/2)+1)):
                if i%j==0:
                    break;
            else:
                    prime_list.append(i)              
    
    return prime_list if (prime_list != []) else "None"
                
number1=int(input("provide first number: "))
number2=int(input("Provide second number: "))

print("prime number in range {} to {}:".format(number1,number2),prime_num_printer(number1,number2))

"""
OUTPUT
provide first number: 8
Provide second number: 10
prime number in range 8 to 10: None

provide first number: 2
Provide second number: 7
prime number in range 2 to 7: [2, 3, 5]
"""