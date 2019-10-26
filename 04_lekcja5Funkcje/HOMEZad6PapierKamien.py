import random

def who_wins(komp, user):
    if komp == user:
        print("Remis")
    elif WINNER_LOSER[komp] == user:
        print("Komputer wygrywa!")
    else:
        print("Wygrałeś!")


def punkty(komp, user):
    if komp == user:
        return 0
    elif WINNER_LOSER[komp] == user:
        return -1
    else:
        return 1

def run_again():
    while True:
        a = input('Run again? (y/n): ')
        if a in ('y', 'n'):
            break
        print('Invalid input.')

    return a


WINNER_LOSER = {
        "k": "n",
        "n": "p",
        "p": "k"
}

wybor = ["k", "p", "n"]

while True:
    komp = random.choice(wybor)
    user = input("\nWybierz k - kamień, p - papier lub n - nożyce\n\t")
    print("Komputer:", komp, ", użytkownik:", user)

    who_wins(komp, user)
    points = punkty(komp, user)
    print("Twoje punkty:", points)

    answer = run_again()
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break