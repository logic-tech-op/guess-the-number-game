import random
import time

n = int(random.randint(0, 100)) 

print("You Have Decided to play the most interesting game, i.e, Guess the Number Game.")
time.sleep(2)


def eHighscore():

    f = open("eHighscore.txt", "a")
    f.write(eScore)
    f.write("\n")
    f.close()

    f = open("eHighscore.txt")
    eRecord = f.readlines()
    print("Best Score is", min(eRecord))
    f.close()

def mHighscore():

    f = open("mHighscore.txt", "a")
    f.write(mScore)
    f.write("\n")
    f.close()

    f = open("mHighscore.txt")
    mRecord = f.readlines()
    print("Best Score is", min(mRecord))
    f.close()

def hHighscore():

    f = open("hHighscore.txt", "a")
    f.write(hScore)
    f.write("\n")
    f.close()

    f = open("hHighscore.txt")
    hRecord = f.readlines()
    print("Best Score is", min(hRecord))
    f.close()

def final():
    
    last = input(
        "If you want to continue playing, type 'Play' or if you want to quit, type 'Quit' : ")
    last = last.capitalize()

    if last == "Play":
        mMenu()

    elif last == "Quit":
        exit()

def mMenu():
    
    menu = input(
        "Type and enter an option from the following --> 'Play' or 'Rules' : ")
    menu = menu.capitalize()

    if menu == "Play":
        cDifficulty()  

    if menu == "Rules":
        time.sleep(0.5)
        print("Rules are as Follows :")
        time.sleep(2)
        print("1. There is a randomly generated Number between 1 and 100. The Goal is to guess that Number with given number of guesses")
        time.sleep(2)
        print("2. Hints Will be given after you make a guess in order to help you guess the number")
        time.sleep(2)
        print("3. You can Choose from 3 Difficulty Levels - Easy , Medium, Hard")
        time.sleep(2)
        print("4. Easy - You have 10 attempts to guess the number\nMedium - You have 7 attempts to guess the number\nHard - You have 5 attempts to guess the number")
        print()

        rMenu = input(
            "That's it. Type and Enter 'Play' if you want to start the game or Type and Enter 'Back' if you want to go to main menu : ")
        rMenu = rMenu.capitalize()

        if rMenu == "Play":
            cDifficulty()

        elif rMenu == "Back":
            mMenu()

def cDifficulty():

    time.sleep(0.5)
    print("Choose a Difficulty Level")
    time.sleep(0.5)
    print("Easy\nMedium\nHard")
    time.sleep(2)
    print()
    level = input("Enter Chosen Difficulty Level if you are ready : ")
    level = level.capitalize()

    if level == "Easy":
        lvlEasy()

    elif level == "Medium":
        lvlMedium()

    elif level == "Hard":
        lvlHard()

def lvlEasy():

    print("You Have Chosen Easy Difficulty")
    time.sleep(0.5)
    print("You Will get 10 Attempts to guess the Number. Game will Start in 3 Seconds")
    time.sleep(3)
    gEasy = 10

    while gEasy > 0:

        numEasy = int(input("Enter a Number : "))

        if numEasy > n:
            print("The Required No. is less than the entered No. You have",
                  gEasy - 1, "guesses left")
            gEasy = gEasy - 1
            continue

        elif numEasy < n:
            print("The Required No. is greater than the entered No. You have",
                  gEasy - 1, "guesses left")
            gEasy = gEasy - 1
            continue

        elif numEasy == n:
            global eScore
            eScore = str(11 - gEasy)
            print("Congratulations ! You guessed the No. in", eScore, "guesses")
            eHighscore()  
            time.sleep(1)
            final()  
            break

    if gEasy == 0:
        print("You Ran out of Guesses. GAME OVER !")
        final() 

def lvlMedium():

    print("You Have Chosen Medium Difficulty")
    time.sleep(0.5)
    print("You Will get 7 Attempts to guess the Number. Game will Start in 3 Seconds")
    time.sleep(3)
    gMedium = 7

    while gMedium > 0:

        numMedium = int(input("Enter a Number : "))

        if numMedium > n:
            print("The Required No. is less than the entered No. You have",
                  gMedium - 1, "guesses left")
            gMedium = gMedium - 1
            continue

        elif numMedium < n:
            print("The Required No. is greater than the entered No. You have",
                  gMedium - 1, "guesses left")
            gMedium = gMedium - 1
            continue

        elif numMedium == n:
            global mScore
            mScore = str(8 - gMedium)
            print("Congratulations ! You guessed the No. in", mScore, "guesses")
            mHighscore() 
            final()  
            break

    if gMedium == 0:
        print("You Ran out of Guesses. GAME OVER !")
        final() 

def lvlHard():

    print("You Have Chosen Hard Difficulty")
    time.sleep(0.5)
    print("You Will get 5 Attempts to guess the Number. Game will Start in 3 Seconds")
    time.sleep(3)
    gHard = 5

    while gHard > 0:

        numHard = int(input("Enter a Number : "))

        if numHard > n:
            print("The Required No. is less than the entered No. You have",
                  gHard - 1, "guesses left")
            gHard = gHard - 1
            continue

        elif numHard < n:
            print("The Required No. is greater than the entered No. You have",
                  gHard - 1, "guesses left")
            gHard = gHard - 1
            continue

        elif numHard == n:
            global hScore
            hScore = str(6 - gHard)
            print("Congratulations ! You guessed the No. in", hScore, "guesses")
            hHighscore()  
            final() 
            break

    if gHard == 0:
        print("You Ran out of Guesses. GAME OVER !")
        final() 


mMenu() 
