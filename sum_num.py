"""Python code to add 2 numbers"""

def sum_num(num1,num2):
    return print("Result of ",num1,"+",num2,"=",num1+num2)

number1=int(input("Enter fisrt number: "))
number2=int(input("Enter Second number: "))

sum_num(number1,number2)

"""
Output
Enter fisrt number: 12
Enter Second number: 12
Result of  12 + 12 = 24

Enter fisrt number: -12
Enter Second number: 12
Result of  -12 + 12 = 0

Enter fisrt number: 10
Enter Second number: 20
Result of  10 + 20 = 30
"""