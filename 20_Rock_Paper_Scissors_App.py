# -*- coding: utf-8 -*-
"""
Created on Sat May 16 01:56:06 2020

@author: mitta anand
"""
import random
print("Welcome to Rock, Paper, Scissors App")

num=int(input("No of Rounds: "))
lis=['rock','paper','scissors']
comp=0
user=0
for i in range(num):
    print("Round",i+1)
    print("User: {}\t Computer: {}".format(user,comp))
    n=random.randint(0,2)
    c=lis[n]
    opt=input("enter users choice: ")
    u=opt.lower()
    print("Computer: ",c)
    print("User: ",u)
    if u in lis:
        if u==c:
            print("its a tie and no one gets point")
        elif u=='paper' and c=='rock':
            print("paper covers rock")
            w='user'
            user+=1
        
        elif u=='scissors' and c=='rock':
            print("Rock smashes scissor")
            w='computer'
            comp+=1

        elif u=='rock' and c=='paper':
            print("paper covers rock")
            w='computer'
            comp+=1
        
        elif u=='scissors' and c=='paper':
            print("scissors cuts paper")
            w='user'
            user+=1

        elif u=='rock' and c=='scissors':
            print("Rock smashes scissor")
            w='user'
            user+=1
        
        elif u=='paper' and c=='scissors':
            print("scissors cuts paper")
            w='computer'
            comp+=1
        
        elif u==c:
            print("It's a tie")
        
        print("winner is: ",w)
        print()

    elif u not in lis:
        print("invalid entry by user. computer gets a point")
        comp+=1
print()
print("final results")
print("Rounds played: ",num)
print("Computer wins: ",comp)
print("User wins: ",user)
if comp>user:
    print("Computer won the game")
else:
    print("User won the game")
