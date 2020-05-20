# -*- coding: utf-8 -*-
"""
Created on Fri May 15 17:18:59 2020

@author: mitta anand
"""

num_strings=['15','100','55','42']
num_ints=[15,100,55,42]
num_floats=[2.2,100.658,32.0,66.79]
num_lists=[[1,2,3],[4,5,6],[7,8,9],[10,11,12,13]]

print('----------------summary-----------------')
print("Type of num_strings is:",type(num_strings))
print("Values in num_strings are:",num_strings)
print("Type of 1st element of num_strings is:",type(num_strings[0]))
print()
print("Type of num_ints is:",type(num_ints))
print("Values in num_ints are:",num_ints)
print("Type of 1st element of num_ints is:",type(num_ints[0]))
print()
print("Type of num_floats is:",type(num_floats))
print("Values in num_floats are:",num_floats)
print("Type of 1st element of num_floats is:",type(num_floats[0]))
print()
print("Type of num_lists is:",type(num_lists))
print("Values in num_lists are:",num_lists)
print("Type of 1st element of num_lists is:",type(num_lists[0]))
print()
num_strings.sort()
num_ints.sort()
print("Sorted strings list:",num_strings)
print("Sorted ints list:",num_ints)