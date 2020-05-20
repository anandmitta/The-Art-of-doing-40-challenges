# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:11:22 2020

@author: mitta anand
"""

print("Grade Point Average Calculator App")
lis=[]
n=int(input("No of grades the user want to input: "))

for i in range(n):
    a=int(input("Enter the grade value: "))
    lis.append(a)
lis.sort()
print("grades from high to low")
sum=0
for i in lis:
    sum+=i
    print("\t",i)
avg=sum/len(lis)
print("Grade point average = ",avg)

desired=int(input("desired average"))
des=desired*(len(lis)+1)-sum
print("you must get {} in next assignment".format(des))
lis1=lis.copy()
ch=int(input("enter the value you want to change"))
r=lis1.index(ch)
new=int(input("enter new value to be replaced"))
lis1[r]=new
csum=0
for i in lis1:
    csum+=i
cavg=csum/len(lis1)
print(cavg)
difference=cavg-avg
print("you have a difference of",difference)
