from random import randint
from main import dif


def generate_sequence():
    genList = []
    for i in range(dif):
        num = randint(1, 101)
        genList.append(num)
    return genList


def get_list_from_user():
    userGenList = []
    for i in range(dif):
        print(f"Enter a integer number ({i+1}/{dif}): ", end="")
        num = input()
        num = int(num)
        userGenList.append(num)
    return userGenList


def is_list_equal(list1, list2):
    list1.sort()
    list2.sort()
    if list1 != list2:
        return False
    return True


def play():
    generatedList = generate_sequence()
    userList = get_list_from_user()
    final_result = is_list_equal(generatedList, userList)
    if not final_result:
        print("You lose... ☹")
        print(f"The generatedList is: {generatedList}")
    else:
        print("You win!!! 😀")
        print(f"The generatedList is: {generatedList}")


play()
