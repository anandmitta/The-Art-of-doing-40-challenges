# -*- coding: utf-8 -*-
"""
Created on Sat May 16 01:17:21 2020

@author: mitta anand
"""

print("Welcome to Voter Registration App")

name=input("Please enter your name: ")
age=int(input("PLease enter your age: "))
lis=['Republican','Democratic','Independent','Libertarian','Green']
if age>=18:
    print("You are eligible to register")
    print("Parties available to register are")
    for i in lis:
        print("\t-{}".format(i))
    
    opt=input("please enter your desired party: ")
    while opt.title() not in lis:
        print("party not available")
        opt=input("Enter correct party: ")
    print("Congratulations you have registered for {} party".format(opt.title()))
    
else:
    print("you are not eligible")