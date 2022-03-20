from os import system


def check_victory(victory):
    if victory is False:
        print("Would you like to restart the game? (Y/N): ", end="")
        answer = input()
        while answer.upper() != 'Y' and answer.upper() != 'N':
            print("Please enter (Y/N): ", end="")
            answer = input()
        if answer.upper() == 'Y':
            system("python main.py \n")
        else:
            print("See you next time...")
            exit()
