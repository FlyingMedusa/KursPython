# Ogrodnik. Utwórz program - udający poradnik ogrodnika.
# Powinen zawierać dowolny słownik przypominający o obowiązkach ogrodniczych w zależności od miesiąca:
# np. styczeń - bielenie pni drzew, październik - czas posadzić wiosenne krzewy.
# Użytkownik może podać skróconą, 3 literową nazwę miesiąca i otrzymać poradę.
# Użytkownik kończy korzystanie z programu naciśnięciem przycisku - Q.

def get_month():
    while True:
        miesiac = input("Podaj nazwę miesiąca jako 3 litery: ")
        if len(miesiac) != 3 or not miesiac.isalpha():
            input("Nie pykło - ")
        else:
            break
    return miesiac.capitalize()

seasonal_dict = {
    "Sty": "bielenie pni drzew",
    "Lut": "sypanie solą bo ślisko",
    "Mar": "Dbanie o przebiśniegi",
    "Kwi": "Zrywanie tulipanów",
    "Maj": "Zrywanie konwalii",
    "Cze": "Wysadzamy petunie",
    "Lip": "Skracanie pędów",
    "Sie": "zjadamy maliny",
    "Wrz": "Zbieramy kasztany",
    "Paź": "Zrywamy dynie",
    "Lis": "Grabimy liście",
    "Gru": "Dokarmiamy sikorki"
}

while True:
    month = get_month()

    if month in seasonal_dict:
        print(seasonal_dict[month])
    else:
        print("Nie znam tego miesiaca")

    user_input = input("Czy chcesz kolejna porade: Y / N: ")
    if user_input.upper() == 'N':
        break
