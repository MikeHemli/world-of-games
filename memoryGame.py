from random import randint


def generate_sequence(dif):
    genList = []
    for i in range(dif):
        num = randint(1, 101)
        genList.append(num)
    return genList


def get_list_from_user(dif):
    userGenList = []
    for i in range(dif):
        print(f"Enter a integer number ({i + 1}/{dif}): ", end="")
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


def play(difficulty):
    generatedList = generate_sequence(difficulty)
    userList = get_list_from_user(difficulty)
    final_result = is_list_equal(generatedList, userList)
    if not final_result:
        print("You lose... ☹")
        print(f"The generatedList is: {generatedList}")
    else:
        print("You win!!! 😀")
        print(f"The generatedList is: {generatedList}")
