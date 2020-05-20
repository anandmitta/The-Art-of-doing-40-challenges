# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:03:41 2020

@author: mitta anand
"""

print(" Frequency Analysis App ")
for j in range(2):
    d={}
    lis=[]
    n=input("Enter any word or phrase: ").lower()
    alphabets=0
    for i in n:
        if i.isalpha():
            alphabets+=1
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
    print("Alphabet\tOccurances\tPercentage")
    for k,v in d.items():
        per=(v/alphabets)*100
        print('{}\t\t{}\t\t{}%'.format(k,v,per))
    
    #sort dictionary based on values
    for k in sorted(d,key=d.get,reverse=True):
        lis.append(k)
    
    print("".join(lis))
        