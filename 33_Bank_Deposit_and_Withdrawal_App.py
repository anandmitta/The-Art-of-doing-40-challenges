# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:02:47 2020

@author: mitta anand
"""

def deposit(amt,d,acc,name):
    d[acc]+=amt
    print("Deposited {} into {} {} account.".format(amt,name,acc))
    
def withdrawal(amt,d,acc,name):
    if d[acc]>0 and amt<d[acc]:
        d[acc]-=amt
        print("Withdrawed {} from {} {} account.".format(amt,name,acc))
    
    else:
        print("Insufficient Funds")


def info(name,d):
    print("Current Account Information")
    print("Name: ",name)
    print("Savings: ",d['savings'])
    print("Current: ",d['current'])
    
print("Bank Deposit and Withdrawal App")
d={'savings':0.0,'current':0.0}

name=input("Please enter your name according to your bank account: ").lower()
s=float(input("How much money would you like to set up your savings account with: "))
c=float(input("How much money would you like to set up your current account with: "))

d['savings']=s
d['current']=c

while(True):
    info(name,d)
    acc=input("What account would you like to access (Savings or Current): ").lower()
    opt=input("What type of transaction would you like to make (Deposit or Withdrawal): ").lower()
    amt=float(input("How much amount: "))
    if opt=='deposit':
        deposit(amt,d,acc,name)
    
    elif opt=='withdrawal':
        withdrawal(amt,d,acc,name)
    
    else:
        print("Invalid option. Try Again")
    
    choice=input("Do you want to make other transaction (y/n): ").lower()
    if choice=='n':
        info(name,d)
        break

print("Thank You")
