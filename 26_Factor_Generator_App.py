# -*- coding: utf-8 -*-
"""
Created on Sat May 16 23:46:38 2020

@author: mitta anand
"""

print("Welcome to Factor Generator App")
while(True):
    n=int(input("Enter the nuumber to find the factors: "))
    factors=[]
    for i in range(1,n+1):
        if n%i==0:
            print(i)
            factors.append(i)
        
    for i in range(int(len(factors)/2)):
        print("{} * {} = {}".format(factors[i],factors[-i-1],n))
    
    
    opt=input("Do you want to enter another number [y|n]: ").lower()
    if opt=='n':
       break
print("Thank you")
            
    
        