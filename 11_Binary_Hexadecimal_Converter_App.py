# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:43:33 2020

@author: mitta anand
"""

print("Binary Hexadecimal Converter App")
n=int(input("Enter decimal number: "))
dec=[]
b=[]
h=[]
for i in range(1,n+1):
    dec.append(i)
    x=bin(i)
    y=hex(i)
    b.append(x)
    h.append(y)

print("Lists generated!!!!!!")

ss=int(input("Enter slicing starting number: "))
se=int(input("Enter slicing ending number: "))

print("decimal values from {} to {}".format(ss,se))
for i in dec[ss:se+1]:
    print(i)

print("binary values from {} to {}".format(ss,se))
for i in b[ss:se+1]:
    print(i)

print("hexadecimal values from {} to {}".format(ss,se)) 
for i in h[ss:se+1]:
    print(i)


n=input("press enter to print all data.")

for d,bi,he in zip(dec,b,h):
    print(d,'-----',bi,'----',he)
