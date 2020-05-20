# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:55:59 2020

@author: mitta anand
"""

print("Welcome to Fibonacci Calculator App ")

n=int(input("Number of fibonacci numbers to display: "))
lis=[]
rat=[]
a,b=0,1
for i in range(1,n+1):
    a,b=b,a+b
    lis.append(a)
    print(a)

print()
print("Golden ration values")
for i in range(len(lis)-1):
    a=lis[i+1]/lis[i]
    rat.append(a)
for i in rat:
    print(i)