from os import system
from live import load_game, welcome
from Scores.score import add_score

print(welcome())
results = load_game()

victory = results[1]
if victory is False:
    print("Would you like to restart the game? (Y/N): ", end="")
    answer = input()
    while answer.upper() != 'Y' and answer.upper() != 'N':
        print("Please enter (Y/N): ", end="")
        answer = input()

    if answer.upper() == 'Y':
        system("python main.py \n")
    else:
        exit()

add_score(victory)
