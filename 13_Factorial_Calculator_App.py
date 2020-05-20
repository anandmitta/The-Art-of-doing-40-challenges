# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:29:16 2020

@author: mitta anand
"""

import math
print("Welcome to Factorial Calculator App")
n=int(input("Enter the number to find the factorial: "))
print("{}!={}".format(n,n),end='')
i=0
r=n-1
while(r>i):
    print('*',r,end='')
    r-=1
print()
default=math.factorial(n)
print("default values is:",default)

i=0
total=1
while(n>i):
    total*=n
    n-=1
print("My code:", total)

if default==total:
    print("same")
else:
    print("Wrong answer")
