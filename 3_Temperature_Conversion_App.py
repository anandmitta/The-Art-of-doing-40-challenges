# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:08:06 2020

@author: mitta anand
"""

print("Welcome to Temperature Conversion App.")

fah=float(input("Enter temperature in Fahrenheit: "))
cel=(fah-32)*(5/9)
kel=fah+273.15
fah1=round(fah,4)
cel1=round(cel,4)
kel1=round(kel,4)
print("Degress in Fahrenheit:\t",fah1)
print("Degress in Celsius:\t",cel1)
print("Degress in Kelvin:\t",kel1)