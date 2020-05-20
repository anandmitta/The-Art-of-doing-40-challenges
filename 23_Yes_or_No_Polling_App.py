# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:09:21 2020

@author: mitta anand
"""

print("Welcome to  Yes or No Polling App")

issue=input("Issue that the voters will be voting on: ")
n=int(input("Number of voters that will be allowed to vote: "))
pwd=input("password to be used to view the polling results: ")
pos=0
neg=0
d={}
for i in range(n):
    name=input("Enter your name: ")
    if name in d.keys():
        print("Sorry, it seems that someone with that name has already voted.")
    else:
        print("Here is the issue:",issue)
        vote=input("What do you think...yes or no: ").lower()
        if vote=='yes':
            d[name]=vote
            pos+=1
        elif vote=='no':
            d[name]=vote
            neg+=1
        else:
            d[name]=vote
            print('That is not a yes or no answer, but okay... ')
        
        print('Thank you {}! Your vote of {} has been recorded.'.format(name,vote))
print('The following people voted')
for i in d.keys():
    print(i)

print("On the following issue:",issue)
if pos==neg:
    print("it was a tie with {} votes".format(pos))
elif pos>neg:
    print("yes leads the votes with {} votes".format(pos))
elif pos<neg:
    print("No leads the votes with {} votes".format(neg))

results=input("To see the voting results enter the admin password: ")
if pwd==results:
    for k,v in d.items():
        print("Voter: {}\tvote: {}".format(k,v))
else:
    print("Wrong password")
print("Thank You")
    
