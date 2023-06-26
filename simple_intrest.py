"""Python Program for simple interest
Simple interest formula is given by: 
Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate"""

def calc_Simple_intrest(amount,time,rate):
    return print("Your Simple Intrest on amount",amount,"for",time,"years, with rate%",rate,"will be",((amount*time*rate)/100))
    
p_amount=int(input("Provide your Amount:"))
time_period=int(input("for time:"))
rate=int(input("with rate:"))

calc_Simple_intrest(p_amount,time_period,rate)

"""
Output
Provide your Amount:10000
for time:5
with rate:5
Your Simple Intrest on amount 10000 for 5 years, with rate 5 will be 2500.0

Provide your Amount:3000
for time:1
with rate:7
Your Simple Intrest on amount 3000 for 1 years, with rate% 7 will be 210.0

"""