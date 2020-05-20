# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:59:31 2020

@author: mitta anand
"""

import random
print("Welcome to The Python Dice App")

def roll():
    dice=int(input("Enter the sides of dice that you want: "))
    turns=int(input("Enter number of turn you want to roll the dice: "))
    lis=[]
    sum=0
    for i in range(turns):
        
        value=random.randint(1,dice)
        lis.append(value)
        sum+=value
    
    print('You rolled {} {} sided dice'.format(turns,dice))
    print("-----Results are as followed-----")
    for i in lis:
        print('\t',i)
    print("The total value of your roll is",sum)
    

while(True):
    roll()
    opt=input("Would you like to roll again (y/n): ")
    if opt=='n':
        break

print("Thank You")