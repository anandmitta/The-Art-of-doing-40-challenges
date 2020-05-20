# -*- coding: utf-8 -*-
"""
Created on Fri May 15 17:35:43 2020

@author: mitta anand
"""
import datetime
lis=['Meat','Cheese']
time=datetime.datetime.now()
month=str(time.month)
day=str(time.day)
hour=str(time.hour)
minute=str(time.minute)
print("current date and time is: {}/{}\t{}:{}".format(day,month,hour,minute))
print(lis)
for i in range(3):
    n=input("Enter an item to insert into list: ")
    lis.append(n.title())
print("updated list is:",lis)
lis.sort()
print("Sorted list:",lis)

for i in range(3):
    print('length of list is:',len(lis))
    r=input("Enter the food purchased: ")
    s=r.title()
    lis.remove(s)
    print("updated list",lis)

if len(lis)==2:
    print(lis)
    print("Store is out of",lis[1])
    lis.remove(lis[1])

user=input("What food do you like: ")
lis.insert(0,user.title())
print(lis)