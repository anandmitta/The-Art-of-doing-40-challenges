# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:12:59 2020

@author: mitta anand
"""
import cmath

print("Welcome to Quadratic Equation Solver App")
n=int(input("No of quadratic equations to solve: "))

for i in range(n):
    
    print("Solving equation",i+1)
    print("---------------------------")
    a=float(input("Please enter your value of a (coefficient of x^2): "))
    b=float(input("Please enter your value of b (coefficient of x): "))
    c=float(input("Please enter your value of c (coefficient): "))
    
    print("The solution for {}x^2+{}x+{}=0 is".format(a,b,c))
    x1=(-b+cmath.sqrt(b**2 - 4*a*c))/(2*a)
    x2=(-b-cmath.sqrt(b**2 - 4*a*c))/(2*a)
      
    print("x1 =",x1)
    print("x2 =",x2)
    print()
    
print("Thank You for using this app")
