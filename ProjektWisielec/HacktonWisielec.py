#- Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
#- Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
#- Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
#- W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć hasło.
import random

def random_slogan():
    secret_word = random.choice(words)
    return secret_word


def storing_letters(letter):
    guessed_letters.append(letter)


HANGMAN = (
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
    |             | |
    |             | |
    |
    |
    |
    -----------------
    """
)


print("\nWelcome to the HANGMAN game!")

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


with open(filename, 'r', encoding='utf-8') as fopen:
    words = fopen.read()
words = words.split()

secret_word = random_slogan()
moves = 10
secret_len = len(secret_word)
guessed_letters = []
secret_w_list = []
secret_w_list = list(secret_word)
showing_list = ["_"] * secret_len


print("\nOur hint for you:\n\tthe word has",secret_len,"letters!")

i = 0
mistakes = 0
while i < 8:
    user_guess = input("\nGive me a letter:\n\t\t")
    if user_guess in guessed_letters:
        print("You've already chosen this letter!")
    else:
        storing_letters(user_guess)
        is_guessed = False
        if user_guess in secret_word:
            print("You've guessed it right!")
            for j in range(0, secret_len):
                if secret_word[j] == user_guess:
                    showing_list[j] = user_guess
            visible_result = " ".join(showing_list)
            print(visible_result)
            if "_" not in visible_result:
                is_guessed = True
        else:
            print("This letter is not in the secret word!")
            print(HANGMAN[i])
            i += 1

        if is_guessed == True:
            break

print("Hurray")