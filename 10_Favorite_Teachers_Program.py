# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:04:33 2020

@author: mitta anand
"""
def printing(lis):
    print("Your Favourite teachers:",fav)
    #fav.sort()
    print("Your Favourite teachers in alphabetic order:",sorted(fav))
    #fav.sort(reverse=True)
    print("Your Favourite teachers in reverse alphabetic order:",sorted(fav,reverse=True))
    
    print("Your top two teachers are {} and {}".format(fav[0],fav[1]))
    print('Your next two favorite teachers are {} and {}'.format(fav[2],fav[3]))
    print('Your last favorite teacher is:',fav[len(fav)-1])
    print('You have a total of {} favorite teachers'.format(len(fav)))
    



print("Welcome to  Favorite Teachers Program ")
fav=[]
lis=['first','second','third','fourth']

for i in lis:
    n=input("Enter your {} favorite teacher: ".format(i))
    fav.append(n.title())
printing(fav)
print('Oops, {} is no longer your first favorite teacher.'.format(fav[0]))
n=input('Who is your new FAVORITE teacher: ') 
fav.insert(0,n.title())
printing(fav)
print("You've decided you no longer like a teacher.")
n=input("Which teacher would you like to remove from you list: ")
fav.remove(n.title())
printing(fav)
