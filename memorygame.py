# memory game
import time
import random
import string
import os

def cls():
    os.system('cls||clear')

def game():
            global level_number
            global max_tries
            global i
            i = 5 #here you can change the time the user has to memorize the code 
            level_number = 1
            max_tries = 5
            while True:
                tries = 0
                word = []
                try_1 = []
                for _ in range (level_number+2): #here you can change the number of characters your word has per level
                    word_character= random.choices(characters)
                    word.extend(word_character)

                while True:
                    tries += 1 
                    try_1 = []
                    print(f"Level {level_number}")
                    print(f"The word is: {word}")
                    print(f"Try {tries}/{max_tries}")
                    print(f"You have {i} seconds to memorize the word!")
                    time.sleep(i)
                    cls()
                    inputbuffer = input("Press enter to continue\n") 
                    cls()
                    try2 = input("What was the word: ")
                    for elem in try2:
                        try_1.append(elem)
                    if tries == max_tries and try_1 != word:
                        print(f"You just surpassed the max number of tries! You finished in level {level_number}. The code was {word}")
                        conclusion()
                    if try_1 == word:
                        print(f"Congrats! You just passed the level {level_number}. Moving on...")
                        level_number += 1
                        max_tries += 1
                        i += 2
                        break
                    else:
                        print("Incorrect! Try again")

def conclusion():
        print(f"Thanks for playing {playername}! Do you want to play again?")
        restart = input("")
        if restart in conformations:
            print("Ok then, lets restart everything!")
            game()
        else:
            print(f"Ok then {playername}. Have a nice day!")

cls()
conformations = ("y","yes","yeah","yap","yessir","okay","sure")
letters = string.ascii_letters
numbers = string.digits
characters = list(letters+numbers)
print("Welcome to the Memory Game! In this game you will have some random letters and numbers and you will need to rewrite them.")
print("You will have 5 tries per level and you will get a new level every time you pass.")
print("You will also have to remember the capitalization's of each letter and get it correct.\n")

def main():
    start = input("Let's start? ").lower()
    if start not in conformations:
        print("Alright then! Have a good day :)")
    else:
        playername = input("First of all, what's your name? ").title()
        print(f"Ok {playername} let's start then!")
        game()
main()
