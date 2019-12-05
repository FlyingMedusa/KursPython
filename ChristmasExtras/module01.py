

def user_choice():
    while True:
        choice = input("Do you want to give list elements separately or in a list?\n\t[s - separately, l - list]\n\t")
        choice = choice.lower()
        if choice in ('l', 's'):
            return choice
        print('Invalid input.')


def option_separate():
    user_list = []
    while True:
        n_el = int(input("How many elements do you want to add to your list?\t"))
        if n_el > 0:
            for i in range(0, n_el):
                word = input("Give me an element: \n\t")
                user_list.append(word)
            return user_list
        else:
            print("Your list needs to have a positive number of elements!")


def option_list():
    while True:
        user_list = input("Give me a list with elements separated by spaces: ")
        if user_list.lstrip(" ") == "":
            print("You need elements in your list!")
        else:
            user_list = user_list.split(" ")
            return user_list



def user_number(user_list):
    while True:
        elements_number = input("How many elements [counting from the end of your list] do you want to show?\n\t")
        if elements_number.isnumeric():
            elements_number = int(elements_number)
            if elements_number <= len(user_list):
                return int(elements_number)
            else:
                print("You cannot take more arguments than your list has.\n"
                      "You want {} arguments, while your list has only {} arguments!\n".format(elements_number, len(user_list)))
        else:
            print('Invalid input.')


def tail(number, list):
    if number == len(list):
        return list
    else:
        number = -number
        new_list = list[number:]
        return new_list
