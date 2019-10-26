#Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia
# z Visą, MasterCard, a może AmericanExpress.

    #All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.

    #MasterCard numbers either start with the numbers 51 through 55 or
    #with the numbers 2221 through 2720. All have 16 digits.

    #American Express card numbers start with 34 or 37 and have 15 digits.
# 4035300539804083 visa
# 5168441223630339 mastercard
# 371642190784801 american


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

card_number = input("Put your card number here: ")

can_be_card_number = False

if 13 > len(card_number) or 16 < len(card_number):
    print("Wrong number")
else:
    if card_number.isdecimal():
        print("Can be a card number")
        can_be_card_number = True
    else:
        print("Not a number")


if is_visa(can_be_card_number,card_number):
    print("I'm a Visa")
elif is_mastercard(can_be_card_number,card_number):
    print("I'm a Mastercard")
elif is_AmE(can_be_card_number,card_number):
    print("I'm an American Express")
else:
    print("Not known card type")