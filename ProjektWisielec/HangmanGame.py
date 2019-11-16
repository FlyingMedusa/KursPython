import random
import HangmanModule as mod

print("\nWelcome to the HANGMAN game!")

filename = mod.chosen_file()

with open(filename, 'r', encoding='utf-8') as fopen:
    words = fopen.read()
words = words.split()

#some crucial variables, lists
secret_word = random.choice(words)
max_mistakes = len(mod.hangman_display)
secret_len = len(secret_word)
secret_w_list = list(secret_word)
guessed_letters = []
showing_list = ["_"] * secret_len

print("\nOur hint for you:\n\tthe word has",secret_len,"letters!")

i = 0
while i < max_mistakes:
    user_guess = input("\nGive me a letter:\n\t\t")
    if user_guess in guessed_letters:
        print("You've already chosen this letter!")
    else:
        mod.storing_letters(user_guess, guessed_letters)
        if user_guess in secret_word:
            visible_result = mod.guessed_letter(secret_len, secret_word, user_guess,showing_list)
            if "_" not in visible_result:
                print("YOU WON!!")
                break
        else:
            mod.wrong_letter(i)
            i += 1
