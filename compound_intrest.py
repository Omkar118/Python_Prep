"""
Python Program for compound interest
 The formula to calculate compound interest annually is given by: 

A = P(1 + R/100)^t 

Compound Interest = A – P 

A is amount 
P is the principal amount 
R is the rate and 
T is the time span
"""

def calc_compound_interest(Pri_amnt,rate,time):
    Amount=Pri_amnt*(1+(rate/100))**time
    return Amount-Pri_amnt


Principal=int(input("Provide your Principal Amount: "))
Rate=float(input("Provide your % rate: "))
time=int(input("Provide your time span: "))

print("Your Compound Intrest on the Principal Amount",Principal,"for the rate of ",Rate,"% for time span of",time,"=",calc_compound_interest(Principal,Rate,time))

"""
OUTPUT
Provide your Principal Amount: 1200
Provide your % rate: 5.4
Provide your time span: 2
Your Compound Intrest on the Principal Amount 1200 for the rate of  5.4 % for time span of 2 = 133.0992000000001


Provide your Principal Amount: 10000
Provide your % rate: 10.25
Provide your time span: 5
Your Compound Intrest on the Principal Amount 10000 for the rate of  10.25 % for time span of 5 = 6288.946267774416

"""