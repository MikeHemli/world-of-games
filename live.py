def welcome():
    while True:
        print("Enter a username: ", end="")
        name = input()
        str = f"\nHello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play."
        if name.isalpha():
            return str
        else:
            print("""Your name cannnot contain numbers/marks/symbols
            and should be not more than one name without a space in between...""")


def load_game():
    while True:
        print(f"\nPlease choose a game to play:\n"
              f"    1) Memory Game - a sequence of numbers will appear for one second and you have to guess it back\n"
              f"    2) Guess Game - guess a number and see if you chose like the computer\n"
              f"    3) Currency Roulette - try and guess the value of a random amount of USD in ILS")
        print("\nNumber: ", end="")
        try:
            game_num = input()
            game_num = int(game_num)
            if game_num < 1 or game_num > 3:
                print("\nYour number is not in range between 1-3!!!")
            else:
                break
        except ValueError:
            print("\nYour input is not a integer number!!!")

    while True:
        print("\nPlease choose game difficulty level between 1-5: ", end="")
        try:
            dif_level = input()
            dif_level = int(dif_level)
            if dif_level < 1 or dif_level > 5:
                print("\nYour number is not in range between 1-5!!!")
            else:
                break
        except ValueError:
            print("\nYour input is not a integer number!!!")
    return game_num, dif_level
