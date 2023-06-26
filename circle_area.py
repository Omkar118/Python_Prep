"""
Python Program for Program to find area of a circle
Area = pi * r^2
where r is radius of circle 
"""

def cal_circle_area(radius):
    return 3.14*(radius)**2

cir_radius=int(input("Provide the radius of circle: "))

print("Area of Circle is: ",cal_circle_area(cir_radius))

"""
Provide the radius of circle: 5
Area of Circle is:  78.5

Provide the radius of circle: 12
Area of Circle is:  452.16


Provide the radius of circle: 10
Area of Circle is:  314.0
"""