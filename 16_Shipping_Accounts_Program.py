# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:42:32 2020

@author: mitta anand
"""

print("Welcome to Shipping Accounts Program")

lis=['a','b','c','d','e']
username=input("enter the username: ")
if username in lis:
    print("current shipping prices are")
    print('''Shipping orders 0 to 100: $5.10 each 
          Shipping orders 100 to 500: $5.00 each 
          Shipping orders 500 to 1000: $4.95 each 
          Shipping orders over 1000: $4.80 each''')
    
    n=int(input("How many items would you like to ship: "))
    res=0
    if(n>0 and n<=100):
        res=n*5.10
    elif(n>100 and n<=500):
        res=n*5.00
    elif(n>500 and n<=1000):
        res=n*4.95
    elif(n>1000):
        res=n*4.80
    
    print("For shipping {} orders its costs you ${}".format(n,round(res,2)))
    
    opt=input("Do you want to confirm[y|n]: ")
    if opt=="y":
        print("Okay.  Shipping your {} items".format(n))
    elif opt=='n':
        print("Okay, no order is being placed at this time")
    print("Thank you")
     
else:
    print("Invalid Username")

    