"""
This is a hangman game, where a player chooses
a word that another player has to guess correctly
either by using letters to piece together the word
or just by guessing whole words directly. The game
ends when the man is fully drawn.

By: Aaron T****
2/21/18 - 2/25/18

Made with PyCharm
"""

import time
from threading import Thread
import os

letters_guessed = ""
incorrect = 0
guess_word = ""
guess_letter = ""

# "dead" checks if the guesser ran out of guesses
# or if the guesser ran out of time.
dead = False

# Here, a player enters a word to be guessed.
# The code below checks if the word given has
# a space or 1 or less characters.

word = input("Player 1, please enter a word to be guessed: ")
while len(word) <= 1 or " " in word:
    print("Please enter a valid word!")
    word = input("Player 1, please enter a word to be guessed: ")
word_length = "*" * len(word)

while True:
    try:
        timer = int(input("Please enter the amount of seconds you want to give the guesser to guess your word: "))
    except ValueError:
        print("Please enter a valid number!")
        print("")
        continue
    if timer <= 1:
        print("Please enter a number greater than 1!")
        print("")
        continue
    print("")
    print("")
    print("")
    break


# This is the countdown for the
# guesser to start guessing.
def ready_set_go():
    time.sleep(1)
    for i in range(3):
        if i == 0:
            print("Ready?")
            time.sleep(1)
        elif i == 1:
            print("")
            print("Set")
            time.sleep(1)
        elif i == 2:
            print("")
            print("Go!")
            time.sleep(1)


# This is the main timer for the program
def countdown():
    global timer, incorrect, dead, word
    while (timer != 0) and (not dead):
        for i in range(timer):
            if dead:
                break
            else:
                time.sleep(1)
                timer = timer - 1
                if timer == 0:
                    print("")
                    print("")
                    print("Time's up! You lose!")
                    print("The word was: " + word.upper())
    # This immediately exits the program. I would use
    # "sys.exit()" but that only exits out of a thread.
    # I want to kill the whole program.
    os._exit(0)


def hangman():
    global timer, guess_letter, guess_word, letters_guessed, incorrect, word_length, word, dead
    counter = 0
    while True:
        counter = counter + 1
        if counter != 1:
            print("You have " + str(timer) + " seconds left!")
        # Here, a user enters a letter or word as their guess.
        guess = input("Player 2, please enter a letter or word guess: ")
        if dead:
            break
        if len(guess) == 1:
            # The code below makes sure the guesser doesn't guess the
            # same wrong or right letter twice.
            guess_letter = guess
            for i in range(len(letters_guessed.upper())):
                if dead:
                    break
                while ((guess_letter.upper() == letters_guessed[i].upper()) or
                       guess_letter.upper() in letters_guessed.upper()) and (not letters_guessed == "") and (not dead):
                    print("You already guessed this!")
                    print("")
                    print(word_length)
                    print("")
                    print("You have " + str(timer) + " seconds left!")
                    guess = input("Player 2, please enter a letter or word guess: ")
                    if dead:
                        break
                    # Lines 124-127 check to see if the user puts in a word after
                    # guessing the same letter twice, right or wrong. This was
                    # previously a bug, but now squashed.
                    if len(guess) > 1:
                        guess_word = guess
                        guess_letter = ""
                        break
                    else:
                        guess_letter = guess
                break
            letters_guessed = letters_guessed + guess_letter
            guess_word = ""
        if dead:
            break
        if len(guess) > 1:
            guess_word = guess
            guess_letter = ""
        if ((guess_word.upper() != word.upper()) and
                (not guess_letter.upper() in word.upper() or guess_letter.upper() == "")):
            # The code below counts how many times the guesser
            # guessed something wrong. Once the user guesses wrong 7
            # times, the game ends and the guesser loses.
            incorrect = incorrect + 1
            if incorrect == 1:
                print("Wrong!")
                print("")
                print("      ________")
                print("     |        |")
                print("     |        |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("=============")
                print("")
                print(word_length)
                print("")
            elif incorrect == 2:
                print("Wrong!")
                print("")
                print("      ________")
                print("     |        |")
                print("     |        |")
                print("     |        O")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("=============")
                print("")
                print(word_length)
                print("")
            elif incorrect == 3:
                print("Wrong!")
                print("")
                print("      ________")
                print("     |        |")
                print("     |        |")
                print("     |        O")
                print("     |        |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("=============")
                print("")
                print(word_length)
                print("")
            elif incorrect == 4:
                print("Wrong!")
                print("")
                print("      ________")
                print("     |        |")
                print("     |        |")
                print("     |        O")
                print("     |       \|")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("=============")
                print("")
                print(word_length)
                print("")
            elif incorrect == 5:
                print("Wrong!")
                print("")
                print("      ________")
                print("     |        |")
                print("     |        |")
                print("     |        O")
                print("     |       \|/")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("=============")
                print("")
                print(word_length)
                print("")
            elif incorrect == 6:
                print("Wrong!")
                print("")
                print("      ________")
                print("     |        |")
                print("     |        |")
                print("     |        O")
                print("     |       \|/")
                print("     |        -")
                print("     |       |")
                print("     |")
                print("     |")
                print("=============")
                print("")
                print(word_length)
                print("")
            elif incorrect == 7 and timer != 0:
                print("You didn't guess the word! You lose!")
                print("")
                print("      ________")
                print("     |        |")
                print("     |        |")
                print("     |        O")
                print("     |       \|/")
                print("     |        -")
                print("     |       | |")
                print("     |")
                print("     |")
                print("=============")
                print("")
                print(word_length)
                print("")
                print("The word was: " + word.upper())
                dead = True
                break
        else:
            # This code congratulates the guesser if they guessed a word
            # and got the word right.
            if guess_word.upper() == word.upper():
                print("You guessed the word! You win!")
                dead = True
                break
            # This code checks if the letter the guesser guessed a letter
            # that was in the word right. If they did, it replaces it with
            # the "*"
            elif guess_letter.upper() in word.upper():
                for i in range(len(word.upper())):
                    if guess_letter.upper() == word[i].upper() and word_length[i] == "*":
                        word_length = word_length[:i] + guess_letter.upper() + word_length[i + 1:]
                print("")
                print(word_length)
                print("")
                # This code congratulates the guesser if they guessed
                # the word after entering in letters as guesses.
                if word_length == word.upper():
                    print("You guessed the word! You win!")
                    dead = True
                    break


x = Thread(target=countdown)
y = Thread(target=hangman)

print("Player 2, the word is " + str(len(word)) + " characters long!")
print("You have " + str(timer) + " seconds to guess the word!")
print("")
ready_set_go()
print("")

x.start()
y.start()
