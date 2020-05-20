# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:37:36 2020

@author: mitta anand
"""

print("Welccome to letter counting app")

name=input("Enter your name: ")
print("Hi {}, I'll count the letters from your message.".format(name.capitalize()))

m=input("Enter the message: ")
msg=m.lower()
d={}
for i in msg:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
while(True):
    n=input("Enter the character that you want to count: ")
    a=n.lower()
    print("Total no of occurances of '{}' are {}".format(a,d[a]))
    
    rep=input("Do you want to get the count of other characters [yes|no]: ")
    if rep=='no':
        break
print("Thank You")
        
    
    