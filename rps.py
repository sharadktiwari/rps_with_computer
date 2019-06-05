from random import *
import sys
playerwins=0
computerwins=0
winningscore=int(input("enter winning scores = "))
while playerwins<winningscore and computerwins<winningscore:
    print(f"playerwins = {playerwins}\ncomputerwins = {computerwins}")
    print("ROCK.....\nPAPER.....\nSCISSORS.....")
    a=input("enter your choice = ").lower()
    if a=='quit' or a=='q':
        print("OH NO computer wins.....")
        sys.exit()
    x=randint(0,2)
    if x==0:
        b='rock'
    elif x==1:
        b='paper'
    else:
        b='scissors'
    print(f"computer plays = {b}")
    
    if a==b:
        print("It is tie")
    elif a=='rock':
        if b=='scissors':
            print("you won..")
            playerwins+=1
        else:
            print("computer won..")
            computerwins+=1
    elif a=='paper':
        if b=='rock':
            print("player won..")
            playerwins+=1
        else:
            print("computer won..")
            computerwins+=1
    elif a=='scissors':
        if b=='paper':
            print("you won..")
            playerwins+=1
        else:
            print("computer won..")
            computerwins+=1
    else:
        print("enter valid move")

if playerwins==computerwins:
    print("IT IS A TIE.....")
elif playerwins>computerwins:
    print("CONGRATS YO WON......")
else:
    print("OH NO COMPUTER WON.....")

print(f"FINAL SCORES: \nPLAYERWINS = {playerwins} \nCOMPUTERWINS = {computerwins}")
print("THANKYOU FOR PLAYING.....")
