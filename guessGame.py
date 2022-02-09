from random import randint

from main import dif


def generate_number():
    secret_number = randint(0, dif)
    print(f"secret number is: ", secret_number)
    return secret_number


def get_guess_from_user():
    print(f"Guess a number from 1 to {dif}: ", end="")
    num = input()
    num = int(num)
    return num


def compare_results(num1, num2):
    if num1 != num2:
        return False
    return True


def play():
    secret_num = generate_number()
    guess_num = get_guess_from_user()
    final_result = compare_results(secret_num, guess_num)
    if not final_result:
        print("You lose... ☹")
        print(f"The random number: {secret_num}")
    else:
        print("You win!!! 😀")
        print(f"The random number: {secret_num}")


play()
