    # memory game
import time
import random
import string
import os
from turtle import clear
os.system('clear')
letters = string.ascii_letters
numbers = string.digits
char = list(letters+numbers)
print("Welcome to the Memory Game! In this game you will have some random letters and numbers and you will need to rewrite them.")

def main():
    def conclusion():
        restart = input(f"Thanks for playing {playername}! Do you want to play again?\n")
        if restart.startswith("y"):
            print("Ok then, lets restart everything!")
            game()
        else:
            print(f"Ok then {playername}. Have a nice day!")
            exit()
    start = input("Let´s start? ").lower()
    if start.startswith("y"):
        playername = input("First of all, what´s your name? ").title()
        print(f"Ok {playername} lets start then!")
        def game():
            global levelnumber
            global maxtries
            global i
            i = 5                                     #here you can change the time the user has to memorize the code 
            levelnumber = 1
            maxtries = 5
            while True:
                tries = 0
                word = []
                try1 = []
                for _ in range (levelnumber+2):       #here you can change the number of characters your word has per level
                    wordchar= random.choices(char)
                    word.extend(wordchar)

                while True:
                    tries += 1 
                    try1 = []
                    print(f"Level {levelnumber}")
                    print(f"The word is: {word}")
                    time.sleep(i)
                    os.system('clear')
                    print(f"Try {tries}/{maxtries}")
                    try2 = input("What was the word? ")
                    for elem in try2:
                        try1.append(elem)
                    if tries == maxtries and try1 != word:
                        print(f"You just surpassed the max number of tries! You finished in level {levelnumber}. The code was {word}")
                        conclusion()
                    if try1 == word:
                        print(f"Congrats! You just passed the level {levelnumber}. Moving on...")
                        levelnumber += 1
                        maxtries += 1
                        i += 2
                        break
                    else:
                        print("Incorrect! Try again")
        game()
    else:
        print("Alright then! Have a good day :)")
main()