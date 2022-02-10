from random import randint


def generate_number(dif):
    secret_number = randint(0, dif)
    return secret_number


def get_guess_from_user(dif):
    print(f"Guess a number from 1 to {dif}: ", end="")
    num = input()
    num = int(num)
    return num


def compare_results(num1, num2):
    if num1 != num2:
        return False
    return True


def play(difficulty):
    secret_num = generate_number(difficulty)
    guess_num = get_guess_from_user(difficulty)
    final_result = compare_results(secret_num, guess_num)
    if not final_result:
        print("You lose... ☹")
        print(f"The random number is: {secret_num}")
    else:
        print("You win!!! 😀")
        print(f"The random number is: {secret_num}")
