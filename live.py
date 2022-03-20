import sys

import guessGame
import memoryGame


def welcome():
    while True:
        print("Enter a username: ", end="")
        name = input()
        if name.isalpha():
            str = f"\nHello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play."
            return str
        else:
            print("""\nYour name cannot contain numbers/marks/symbols
and should be not more than one name without a space in between...\n""")


def load_game():
    while True:
        print(f"\nPlease choose a game to play:\n"
              f"    1) Memory Game - a sequence of numbers will appear for one second and you have to guess it back\n"
              f"    2) Guess Game - guess a number and see if you chose like the computer\n"
              f"    3) Currency Roulette - try and guess the value of a random amount of USD in ILS")
        print("\nYou selected game number: ", end="")
        try:
            game_number = input()
            game_number = int(game_number)
            if game_number < 1 or game_number > 3:
                print("\nYour number is not in range between 1-3!!!")
            elif game_number == 3:
                print("\nThe Current Roulette Game is not available at the moment...")
                sys.exit()
            else:
                break
        except ValueError:
            print("\nYour input is not a integer number!!!")

    while True:
        print("\nPlease choose game difficulty level between 1-5: ", end="")
        try:
            difficulty_level = input()
            difficulty_level = int(difficulty_level)
            if difficulty_level < 1 or difficulty_level > 5:
                print("\nYour number is not in range between 1-5!!!")
            else:
                break
        except ValueError:
            print("\nYour input is not a integer number!!!")
    if game_number == 1:
        if_victory = memoryGame.play(difficulty_level)
        return difficulty_level, if_victory
    else:
        if_victory = guessGame.play(difficulty_level)
        return difficulty_level, if_victory
