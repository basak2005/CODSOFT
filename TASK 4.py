#INSTRUCTION FOR THIS GAME AND THE PROCEDURE
#THIS IS A NORMAL STONE, PAPER AND SISSORS GAME PLAYED IN THE CHILDHOOD
#RANDOM MODULE IS INVOLVED SO THAT SYSTEM CAN RANDOMLY PICK ANY OF STONE, PAPER OR SISSOR FRO THE GIVEN LIST OF IT
#WIN LOST AND DRAW POSSIBILLITIES ARE AS FOLLOWS:
# COMPUTER                       USER            RESULT(FROM YOUR SIDE)
# STONE/PAPER/SISSOR     STONE/PAPER/SISSOR             DRAW
# STONE                        PAPER                    WIN
# STONE                       SISSOR                    LOST
# SISSOR                       PAPER                    LOST
# SISSOR                       STONE                    WIN
# PAPER                        STONE                    LOST
# PAPER                        SISSOR                   WIN





import random as rd

mylist = ["STONE", "PAPER", "SISSOR"]
win=0
draw=0
lost=0

#instruction--------------
print("-----------------------------------------------")
print("give STONE PAPER or SISSOR as a move")
print("-----------------------------------------------")
turn=int(input("ENTER HOW MUCH TURN DO YOU WANT TO PLAY THIS GAME: "))
i=1
while(i<=turn):
    computer=rd.choices(mylist, weights = [1,1,1], k = 1)
    real="".join(computer)
    print()

    #USER INPUT TAKING-------------------------
    user=input(f"Enter your {i} move: ")

    #CONDITION FOR DRAW GAME--------------------
    if(real==user.upper()):
        print(f"COMPUTER = {real} USER = {user}")
        draw=draw+1
        print("DRAW")

    #CONDITION WHEN SYSTEM CHOOSE STONE------------------
    elif(real=="STONE" and user.upper()=="SISSOR"):
        print(f"COMPUTER = {real} USER = {user}")
        lost+=1
        print("YOU LOST")
    elif(real=="STONE" and user.upper()=="PAPER"):
        print(f"COMPUTER = {real} USER = {user}")
        win+=1
        print("YOU WON")

    #CONDITION WHEN SYSTEM CHOOSE PAPER-----------------
    elif(real=="PAPER" and user.upper()=="STONE"):
        print(f"COMPUTER = {real} USER = {user}")
        lost+=1
        print("YOU LOST")
    elif(real=="PAPER" and user.upper()=="SISSOR"):
        print(f"COMPUTER = {real} USER = {user}")
        win+=1
        print("YOU WON")

    #CONDITION WHEN SYSTEM CHOOSE SISSOR-------------------
    elif(real=="SISSOR" and user.upper()=="STONE"):
        print(f"COMPUTER = {real} USER = {user}")
        win+=1
        print("YOU WON")
    elif(real=="SISSOR" and user.upper()=="PAPER"):
        print(f"COMPUTER = {real} USER = {user}")
        lost+=1
        print("YOU LOST")

    i+=1
print("---------------------------------------------------------------")
print(f"GAME PLAYED {turn}")
print(f"WON  {win} \nDRAW {draw} \nLOST {lost}")