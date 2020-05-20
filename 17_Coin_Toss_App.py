# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:56:12 2020

@author: mitta anand
"""
import random
print("Welcome to Coin Toss App")

n=int(input("No of times to flip the coin: "))
see=input("do you wish to see result of each flip [y|n]: ")
h=0
t=0
for i in range(n):
    toss=random.randint(0,1)
    if toss==0:
        t+=1
    elif toss==1:
        h+=1
    if see.startswith("y" or "Y"):
        print(toss)
    
    if h==t:
        print("it occured at {} flip".format(i+1))
    
per_h=round((h/n)*100,1)
per_t=round((t/n)*100,1)

print("side\t count\t percentage")
print("heads\t {}/{}\t{}%".format(h,n,per_h))
print("tails\t {}/{}\t{}%".format(t,n,per_t))
    