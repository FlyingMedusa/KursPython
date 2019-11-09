def is_visa(is_card, number):
    if is_card == False:
        return False
    if len(number) == 16 or len(number) == 13:
        if card_number[0] == '4':
            return True


def is_mastercard(is_card, number):
    if is_card == False:
        return False
    if len(number) == 16:
        if int(number[0:2]) in range(51, 56) or int(number[0:4]) in range(2221, 2721):
            return True


def is_AmE(is_card, number):
    if is_card == False:
        return False
    if len(number) == 15:
        if int(number[0:2]) in (34, 37):
            return True


filename = 'cardsnumbers.txt'

with open(filename) as fopen:
    cards = fopen.read()

cards = cards.split()
i = 1
for card_number in cards:

    can_be_card_number = False
    print(i)
    if 13 > len(card_number) or 16 < len(card_number):
        print("\tWrong number")
    else:
        if card_number.isdecimal():
            print("\tCan be a card number")
            can_be_card_number = True
        else:
            print("\tNot a number")

    if is_visa(can_be_card_number, card_number):
        print("\tI'm a Visa")
        with open('visa.txt', 'a') as f:
            f.write(card_number)
    elif is_mastercard(can_be_card_number, card_number):
        print("\tI'm a Mastercard")
        with open('mastercard.txt', 'a') as f:
            f.write(card_number)
    elif is_AmE(can_be_card_number, card_number):
        print("\tI'm an American Express")
        with open('American.txt', 'a') as f:
            f.write(card_number)
    else:
        print("\tNot known card type")
    i += 1