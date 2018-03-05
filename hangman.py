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

words_guessed = []
letters_guessed = ""
incorrect = 0
guess_word = ""
guess_letter = ""

# "dead" checks if the guesser ran out of guesses
# or if the guesser guessed the word. Once "dead"
# is True, it stops the timer thread.
dead = False

# Here, a player enters a word to be guessed.
# The code below checks if the word given has
# a space or 1 or less characters.

word = input("Player 1, please enter a word to be guessed: ").upper()
while len(word) <= 1 or not word.isalpha():
    print("Please enter a valid word!")
    print("")
    word = input("Player 1, please enter a word to be guessed: ").upper()
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
                print("The word was: " + word)
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
        while not guess.isalpha():
            print("Please enter a valid guess!")
            print("")
            print(word_length)
            print("")
            print("You have " + str(timer) + " seconds left!")
            guess = input("Player 2, please enter a letter or word guess: ")
        if len(guess) == 1:
            guess_letter = guess.upper()
            # The code below makes sure the guesser doesn't
            # guess the same wrong or right letter twice.
            while guess_letter in letters_guessed:
                print("You already guessed this!")
                print("")
                print(word_length)
                print("")
                print("You have " + str(timer) + " seconds left!")
                guess = input("Player 2, please enter a letter or word guess: ")
                while not guess.isalpha():
                    print("Please enter a valid guess!")
                    print("")
                    print(word_length)
                    print("")
                    print("You have " + str(timer) + " seconds left!")
                    guess = input("Player 2, please enter a letter or word guess: ")
                # The four lines below check to see if the
                # user puts in a word after guessing letters.
                if len(guess) > 1:
                    guess_word = guess.upper()
                    guess_letter = ""
                    break
                else:
                    guess_letter = guess.upper()
                guess_word = ""
            letters_guessed = letters_guessed + guess_letter
        if len(guess) > 1:
            guess_word = guess.upper()
            # The code below makes sure the guesser
            # doesn't guess the same wrong word twice.
            while guess_word in words_guessed:
                print("You already guessed this!")
                print("")
                print(word_length)
                print("")
                print("You have " + str(timer) + " seconds left!")
                guess = input("Player 2, please enter a letter or word guess: ")
                while not guess.isalpha():
                    print("Please enter a valid guess!")
                    print("")
                    print(word_length)
                    print("")
                    print("You have " + str(timer) + " seconds left!")
                    guess = input("Player 2, please enter a letter or word guess: ")
                if len(guess) == 1:
                    guess_letter = guess.upper()
                    guess_word = ""
                    while guess_letter in letters_guessed:
                        print("You already guessed this!")
                        print("")
                        print(word_length)
                        print("")
                        print("You have " + str(timer) + " seconds left!")
                        guess = input("Player 2, please enter a letter or word guess: ")
                        while not guess.isalpha():
                            print("Please enter a valid guess!")
                            print("")
                            print(word_length)
                            print("")
                            print("You have " + str(timer) + " seconds left!")
                            guess = input("Player 2, please enter a letter or word guess: ")
                        if len(guess) > 1:
                            guess_word = guess.upper()
                            guess_letter = ""
                            break
                        else:
                            guess_letter = guess.upper()
                            guess_word = ""
                    letters_guessed = letters_guessed + guess_letter
                else:
                    guess_word = guess.upper()
                    guess_letter = ""
            if guess_word != "":
                words_guessed.append(guess_word)
        if (guess_word != word) and ((guess_letter not in word) or (guess_letter == "")):
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
            elif incorrect == 7:
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
                print("The word was: " + word)
                dead = True
                break
        else:
            # This code congratulates the guesser if they guessed a word
            # and got the word right.
            if guess_word == word:
                print("You guessed the word! You win!")
                dead = True
                break
            # This code checks if the letter the guesser guessed a letter
            # that was in the word right. If they did, it replaces it with
            # the "*"
            elif guess_letter in word:
                for i in range(len(word)):
                    if guess_letter == word[i] and word_length[i] == "*":
                        word_length = word_length[:i] + guess_letter + word_length[i + 1:]
                print("")
                print(word_length)
                print("")
                # This code congratulates the guesser if they guessed
                # the word after entering in letters as guesses.
                if word_length == word:
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
