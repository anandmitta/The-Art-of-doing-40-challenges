# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:27:37 2020

@author: mitta anand
"""

print("welcome to Basketball Roster Program")
lis=[]
pos=['Point Guard','Shooting Guard','Small Forward','Power Forward','Center']
for i in range(len(pos)):
    n=input("Enter player for {} position: ".format(pos[i]))
    lis.append(n.title())
    
print("your starting 5 for upcoming basketball session")
for i in range(len(lis)):
    print("\t{}:\t{}".format(pos[i],lis[i]))

n=input("Enter name of the injured player: ")
n1=n.title()
r=lis.index(n1)
if n1 in lis:
    lis.remove(n1)
print("Oh!!!! Sorry.....{} is injured".format(n1))
rep=input("Enter the name of player to replace: ")
lis.insert(r,rep.title())
print("your starting 5 for upcoming basketball session")
for i in range(len(lis)):
    print("\t{}:\t{}".format(pos[i],lis[i]))
 