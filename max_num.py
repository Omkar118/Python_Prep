"""Maximum of two numbers in Python"""
def max_number(num1,num2):
    return "Both the numbers are equal " if (num1==num2) else print(max(num1,num2), " is Bigger number")


number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
max_number(number1,number2)

"""
Output
Enter the first number: -200
Enter the second number: -200
'Both the numbers are equal '

Enter the first number: 100
Enter the second number: 200
200  is Bigger number

"""