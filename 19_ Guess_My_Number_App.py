# -*- coding: utf-8 -*-
"""
Created on Sat May 16 01:29:30 2020

@author: mitta anand
"""
import random
print("Welcome to  Guess My Number App")

name=input("Enter name: ")
print("hi {}, I am thinking of a number between 1 and 20.".format(name))
count=0
num=random.randint(1,20)
print(num)
for i in range(5):
    guess=int(input("Enter your guess: "))
    if guess>num:
        print("Too High")
    elif guess<num:
        print("Too Low")
    
    elif num==guess:
        print("congrats you guessed in {} turns".format(i+1))
        break
    
    if(i==4):
        print("Game Over")
    