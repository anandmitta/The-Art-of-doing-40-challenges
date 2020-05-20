# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:15:28 2020

@author: mitta anand
"""

print("Even Odd Number Sorter App")

while(True):
    odd=[]
    even=[]
    n=[int(i) for i in input("Enter Sequence of numbers ',' seperated: ").split(",")]
    for i in n:
        if i%2==0:
            print(i,"is even!")
            even.append(i)
        else:
            print(i,"is odd!")
            odd.append(i)
    print()
    print("odd numbers are")
    for i in sorted(odd):
        print("\t",i)
    print()
    print("Even numbers are")
    for i in sorted(even):
        print("\t",i)
    print()
    opt=input("Do you want to run again[y|n]: ").lower()
    if opt=='n':
        break
    
print("Thank You")