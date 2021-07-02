import random
import time

cont=True
def main():
    player=int(input("Please make your choice by entering the number:\n(1) Paper\n(2) Scissor\n(3) Rock\n"))
    cp=random.randint(1,3)

    if player==1:
        print("You use paper!")
        if cp==1:
            print("Computer uses paper!\nDraw!")
        if cp==2:
            print("Computer uses scissors!\nYou lose!")
        if cp==3:
            print("Computer uses rock!\nYou win!")

    elif player==2:
        print("You use scissors!")
        if cp==1:
            print("Computer uses paper!\nYou win!")
        if cp==2:
            print("Computer uses scissors!\nDraw!")
        if cp==3:
            print("Computer uses rock!\nYou lose!")

    elif player==3:
        print("You use rock!")
        if cp==1:
            print("Computer uses paper!\nYou lose!")
        if cp==2:
            print("Computer uses scissors!\nYou win!")
        if cp==3:
            print("Computer uses rock!\nDraw!")
    
    else:
        print("Invalid input")
        main()

    time.sleep(1)

def next():
    while cont==True:
        next_game=(input("Do you want to play again?(Y / N) "))
        if next_game.upper()=="Y":
            main()

        elif next_game.upper()=="N":
            quit()
            
        else:
            print("I do not understand what you mean.")
            next()




main()
next()
