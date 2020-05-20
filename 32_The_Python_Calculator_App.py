# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:28:31 2020

@author: mitta anand
"""

def add(n1,n2):
    result=n1+n2
    print("The sum of {} and {} is {}".format(n1,n2,result))
    lis.append('{} + {} = {}'.format(n1,n2,result))

def sub(n1,n2):
    result=n1-n2
    print("The difference of {} and {} is {}".format(n1,n2,result))
    lis.append('{} - {} = {}'.format(n1,n2,result))

def mul(n1,n2):
    result=n1*n2
    print("The product of {} and {} is {}".format(n1,n2,result))
    lis.append('{} * {} = {}'.format(n1,n2,result))

def div(n1,n2):
    if n2!=0:
        result=n1/n2
        print("The quotient of {} and {} is {}".format(n1,n2,result))        
        lis.append('{} / {} = {}'.format(n1,n2,result))
        
    else:
        print("You cannot divide by zero")
        lis.append("DIV ERROR")

def exp(n1,n2):
    result=n1**n2
    print("The result of {} raised to the {} power is {}".format(n1,n2,result))
    lis.append('{} ** {} = {}'.format(n1,n2,result))

print("The Python Calculator App")
lis=[]
while(True):
    n1=float(input("Enter 1st number: "))
    n2=float(input("Enter 2nd number: "))
    op=input("Enter an operation (addition, subtraction, multiplication, division, or power): ").lower()
    
    if op=='addition' or op=='a':
        add(n1,n2)
    
    elif op=='subtraction' or op=='s':
        sub(n1,n2)
        
    elif op=='multiplication' or op=='m':
        mul(n1,n2)
        
    elif op=='division' or op=='d':
        div(n1,n2)
        
    elif op=='power' or op=='p':
        exp(n1,n2)
    
    else:
        print("That is not a valid operation.  Try again")
        lis.append("OPP ERROR ")
        
    opt=input("Would you like to run the program again (y/n): ").lower()
    if opt=='n':
        print("Calculation Summary:")
        for i in lis:
            print(i)
        break
print()
print("Thank You")
