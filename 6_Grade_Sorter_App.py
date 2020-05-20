# -*- coding: utf-8 -*-
"""
Created on Fri May 15 17:00:52 2020

@author: mitta anand
"""

print("Welcome to Grade Sorter App ")
lis=[]
i=0
while(i<4):
    
    n=int(input("Enter the grade: "))
    lis.append(n)
    i+=1

print("Grades provided are:",lis)
lis.sort(reverse=True)
print("Your grades from highest to lowest are:",lis)
print("The lowest two grades will be dropped")
print("lowest grade is:",lis.pop())
print("Second lowest grade is:",lis.pop())
print("Your remaining grades are:",lis)
print("Your highest grade is:",lis[0])
    