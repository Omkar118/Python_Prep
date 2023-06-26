"""
Print the sum of series 13 + 23 + 33 + 43 + …….+ n3 till n-th term. Examples:

Input : n = 5
Output : 225
13 + 23 + 33 + 43 + 53 = 225

Input : n = 7
Output : 784
13 + 23 + 33 + 43 + 53 + 
63 + 73 = 784
"""

def natural_num_cube(num1):
    result=0
    for i in range (1,num1+1):
        result=result+(i**3)
        
    return result

input_num=int(input("Enter the number to calculate cube of first n natural numbers: "))
print("Sum of cubes of first ",input_num,"natural numbers is:",natural_num_cube(input_num))

"""
OUTPUT
Enter the number to calculate cube of first n natural numbers: 5
Sum of cubes of first  5 natural numbers is: 225

Enter the number to calculate cube of first n natural numbers: 7
Sum of cubes of first  7 natural numbers is: 784

"""