# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:13:50 2020

@author: mitta anand
"""
import random
print("Thesaurus App")

d={"hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'], 
   "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'], 
   "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'], 
   "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']}

print("Values present in dictionary are:")
for i in d.keys():
    print("\t-",i)

n=input("What word would you like a synonym for: ").lower()


print("The synonym for {} is {}".format(n,random.choice(d[n])))

opt=input("Would you like to see the whole thesaurus (yes/no): ")
opt1=opt.lower()
if opt1=='yes':
    for i,j in d.items():
        print("Synonyms available for {} are".format(i))
        for q in j:
            print("\t-",q)
print("I hope you enjoyed the program.  Thank you!")