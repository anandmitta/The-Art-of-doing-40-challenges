# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:23:46 2020

@author: mitta anand
"""
import random
print("Guess My Word App")
while(True):
    d={'sports':['cricket','baseball','football','basketball','hockey'],
       'fruits':['apple','banana','kiwi','grapes','jackfruit'],
       'animals':['tiger','dog','cat','rat','lion']}
    category=random.choice(list(d))
    element=random.choice(d[category])
    rep=list(len(element)*'-')
    print("Guess a {} letter word from the following category: {}\n{}".format(len(element),category,''.join(rep)))
    count=1
    while(True):
        guess=input("Enter your guess: ").lower() 
        if guess==element:
            print("Element: ",element)
            print("You have guessed in {} guesses.".format(count))
            break
        else:
            count+=1
            print("Sorry wrong guess.")
            index=random.randint(0,len(element)-1)
            while(rep[index]!='-'):
                index=random.randint(0,len(element)-1)
            ele=element[index]
            rep[index]=ele
            joined="".join(rep)
            print("Here is your clue: ",joined)
            if joined==element:
                print("You have failed")
                break
    opt=input("Do you want guess other word[y|n]: ").lower()
    if opt=='n':
        break
print("Thank You")