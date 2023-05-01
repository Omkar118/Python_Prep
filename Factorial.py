"""
Python Program for factorial of a number
"""
#Recurssion approch
def fact_rec(n):

    return 1 if( n==1 or n==0 ) else n*fact_rec(n-1)

#Normal Approch
def num_facto(a):
    result=1
    loop_counter=0

    while (loop_counter<a):
        result=result*(a-loop_counter)
        loop_counter = loop_counter+1       
    
    return result;

print("num_facto Result for number 15:",num_facto(15))
print("fact_rec Result for number 15: ",fact_rec(15))


"""
num_facto Result for number 15: 1307674368000
fact_rec Result for number 15:  1307674368000

num_facto Result for number 1: 1
fact_rec Result for number 1:  1

num_facto Result for number 5: 120
fact_rec Result for number 5:  120
"""