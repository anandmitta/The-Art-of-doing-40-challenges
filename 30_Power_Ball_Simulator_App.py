# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:54:35 2020

@author: mitta anand
"""
import random
print("Power Ball Simulator App")
win=[]
white=int(input("How many white-balls to draw from for the 5 winning numbers (Normally 69): "))
red=int(input("How many red-balls to draw from for the Power-Ball (Normally 26): "))
if white<5:
    white=5
elif white>69:
    white=69
if red<1:
    red=1
elif red>26:
    red=26
odds=1
for i in range(5):
    odds*=white-i
odds=odds*red/120
print("You have a chance of 1 in {} to win the lottery".format(odds))
pur=int(input("Purchase tickets in what interval: "))
print("---------Welcome to the Power-Ball-----------")
while(len(win)<5):
    s=random.randint(1,white)
    if s not in win:
        win.append(s)
win.sort()
win.append(random.randint(1,red))
print("Today's winning tickets are: ",end='')
for i in win:
    print(i,end=' ')
print()
print("Press Enter to purchase tickets")
count=0
total_tickets=[]
won=[]
flag=True
while(flag):    
    for i in range(pur):
        purchased_ticket=[]
        while(len(purchased_ticket)<5):
            r=random.randint(1,white)
            if r not in purchased_ticket:
                purchased_ticket.append(r)
        purchased_ticket.sort()
        purchased_ticket.append(random.randint(1,red))
        count+=1    
        if purchased_ticket not in total_tickets:
            total_tickets.append(purchased_ticket)    
            print(purchased_ticket)
        elif purchased_ticket in total_tickets:
            print("Got a loosing ticket again")
        
        if purchased_ticket==win:
            print("You won at {}th purchase.".format(count))
            flag=False
            break
    if total_tickets[len(total_tickets)-1]==win:
        break
    opt=input("Do you want to buy more tickets [y|n]: ").lower()
    if opt=='n':
        print("Better luck next time!!!!!")
        break
print("You have tried",count)
print("Thank You")



