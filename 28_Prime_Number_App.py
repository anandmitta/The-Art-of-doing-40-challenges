# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:32:25 2020

@author: mitta anand
"""

print("Prime Number App")

while(True):
    
    print('Enter 1 to determine if a specific number is prime.\nEnter 2 to determine all prime numbers within a set range.')
    opt=int(input("Enter your choice 1 or 2: "))
    print()
    if opt==1:
        n=int(input("Enter a number to determine if it is prime or not: "))
        for i in range(2,n//2):
            if n%i==0:
                print(n,"is not a prime number!!!")
                break
        else:
            print(n,"is prime number.")
    
    if opt==2:
        notp=[]
        p=[]
        l=int(input("Enter Lower Bound: "))
        u=int(input("Enter Upper Bound: "))
        print()
        for i in range(l,u+1):
            
            for j in range(2,i//2):
                if i%j==0:
                    notp.append(i)
                    break
            else:
                p.append(i)
        print("Total no of non-prime numbers between the range {}-{} are: {}".format(l,u,len(notp)))
        print("Total no of prime numbers between the range {}-{} are: {}".format(l,u,len(p)))
    print()
    choice=input("Do you want to run the program again [y|n]: ").lower()
    if choice=='n':
        break
print("Thank You")