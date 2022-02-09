# import guessGame
from live import load_game, welcome


def get_difficulty(someList):
    difficulty = list(someList)
    return difficulty[1]


def get_game_number_selection():
    game_number = list(objects)
    return game_number[0]


welcome()
objects = load_game()
# objects = list(objects)
dif = get_difficulty(objects)
