import random

def chosen_file():
    while True:
        file = input("Choose the type of secret words:\na - animals\nf - food\np - plants\n")
        if file == "a":
            filename = "animals.txt"
            break
        elif file == "f":
            filename = "food.txt"
            break
        elif file == "p":
            filename = "plants.txt"
            break
        else:
            print("Choose 'a' or 'f' or 'p'!")
    return filename

def storing_letters(letter, guessed_letters):
    guessed_letters = guessed_letters.append(letter)
    return guessed_letters

def guessed_letter(secret_len, secret_word, user_guess,showing_list):
    print("That's right!")
    for j in range(0, secret_len):
        if secret_word[j] == user_guess:
            showing_list[j] = user_guess
    visible_result = " ".join(showing_list)
    print(visible_result)
    return visible_result

def wrong_letter(i):
    print("This letter is not in the secret word!")
    print(hangman_display[i])


hangman_display = (
    """
    ----------------
    |              |
    |
    |
    |
    |
    |
    |
    |
    |
    -----------------
    """,
    """
    ----------------
    |              |
    |              O
    |
    |
    |
    |
    |
    |
    |
    -----------------
    """,
    """
    ----------------
    |              |
    |              O
    |             -+-
    |
    |
    |
    |
    |
    |
    -----------------
    """,
    """
    ----------------
    |              |
    |              O
    |            /-+-
    |
    |
    |
    |
    |
    |
    -----------------
    """,
    """
    ----------------
    |              |
    |              O
    |            /-+-/
    |
    |
    |
    |
    |
    |
    -----------------
    """,
    """
    ----------------
    |              |
    |              O
    |            /-+-/
    |              |
    |
    |
    |
    |
    |
    -----------------
    """,
    """
    ----------------
    |              |
    |              O
    |            /-+-/
    |              |
    |             |
    |             |
    |
    |                You have
    |               LAST chance
    -----------------
    """,
    """
    ----------------
    |              |
    |              O
    |            /-+-/
    |              |
    |             | |
    |             | |
    |
    |               guess who's
    |                   DEAD
    -----------------
    """
)