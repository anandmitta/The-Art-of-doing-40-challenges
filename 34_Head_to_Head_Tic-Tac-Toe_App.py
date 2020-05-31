# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:19:14 2020

@author: mitta anand
"""
def output(lis):
    print("Tic-Tac-Toe")
    print("-------")
    print("|{}|{}|{}|".format(lis[0],lis[1],lis[2]))
    print("-------")
    print("|{}|{}|{}|".format(lis[3],lis[4],lis[5]))
    print("-------")
    print("|{}|{}|{}|".format(lis[6],lis[7],lis[8]))
    print("-------")
 
def player_input(pno,ip_lis):
    while(True):
        n=int(input("{}:Where would you like to place your piece (1 - 9): ".format(pno)))
        if n>=0 and n<=9:
            if ip_lis[n-1]!="-":
                print("That spot has already been chosen.  Try again.")
                #n=int(input("{}:Where would you like to place your piece (1 - 9): ".format(pno)))
            else:
                ip_lis[n-1]=pno
                output(ip_lis)
                break
        else:
            print("That is not a spot on the board.  Try again.")
        
def win(pno,n_lis):
    return ((n_lis[0]==pno and n_lis[1]==pno and n_lis[2]==pno) 
        or (n_lis[3]==pno and n_lis[4]==pno and n_lis[5]==pno) 
        or (n_lis[6]==pno and n_lis[7]==pno and n_lis[8]==pno)
        or (n_lis[0]==pno and n_lis[3]==pno and n_lis[6]==pno) 
        or (n_lis[1]==pno and n_lis[4]==pno and n_lis[7]==pno)
        or (n_lis[2]==pno and n_lis[5]==pno and n_lis[8]==pno))
 
p1="X"
p2="O"
n_lis=["-"]*9
actual_list=[int(i) for i in range(1,10)]
output(actual_list)
print()
output(n_lis)
while(True):
    player_input(p1,n_lis)
    if win(p1,n_lis):
        print("Congratulations! Player 1 won the game")
        break
    if "-" not in n_lis:
        print("It's a tie match")
        break
    player_input(p2,n_lis)
    if win(p2,n_lis):
        print("Congratulations! Player 2 won the game")
        break
