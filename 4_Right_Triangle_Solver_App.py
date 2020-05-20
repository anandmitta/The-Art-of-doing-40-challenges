# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:28:21 2020

@author: mitta anand
"""
import math
print("Welcome to Right Triangle Solver App.")

b=float(input("enter base of the triangle: "))
h=float(input("enter height of the triangle: "))

hyp=math.sqrt(b**2+h**2)
area=(1/2)*b*h
hyp1=round(hyp,3)
area1=round(area,3)

print("Hypotenuse is:",hyp1)
print("Area is:",area1)

