haslo = input("Podaj hasło: \n")

dlugosc = len(haslo)
czybrakliter = haslo.isdecimal()
czybrakcyfer = haslo.isalpha()
czybrakduzejlitery = haslo.islower()

if dlugosc < 8:
    print("Twoje hasło jest za krótkie! Musi mieć minimum 8 znaków!")
if czybrakliter == True:
    print("Hasło musi zawierać choć 1 literę!")
if czybrakcyfer == True:
    print("Hasło musi zawierać chociaż jedną cyfrę!")
if czybrakduzejlitery == True:
    print("Hasło musi zawierać choć 1 dużą literę!")
else:
    print("Twoje hasło jest idealne!")