# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:39:06 2020

@author: mitta anand
"""

print("Database Admin Program")

d={'Anand':'anandmitta','Praneeth':'praneeth','Chandan':'chandan','Khizar':'khizarakram','Manish':'kovelamudi'}
un=input("Enter username:\t")
if un not in d.keys():
    print("Invalid Username")
if un in d.keys():
    pwd=input("Enter password:\t")
    if pwd==d[un]:
        print("Hi you have logged in!!!!")
        opt=input("Do you want to change your password [yes|no]: ").lower()
        if opt=='yes':
            pwd1=input("Enter new password: ")
            if len(pwd1)<8:
                print("Password should be greater than or equal to 8 characters")
                pwd1=input("Enter password greater than or equal to 8 characters: ")
            
            d[un]=pwd1
            print("Password changed!!!")
    
    else:
        print("Wrong password!!!!")


        
        

