# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:59:48 2020

@author: mitta anand
"""

print("Welcome to Multiplication/Exponent Table App.")

n=float(input("Enter a number: "))

print("Multiplication Table results are:")
for i in range(1,10):
    m=i*n
    m1=round(m,4)
    print("\t{}*{} = {}".format(i,n,m1))

print("Exponent Table results are:")
for i in range(1,10):
    m=n**i
    m1=round(m,4)
    print("\t{}**{} = {}".format(i,n,m1))
    