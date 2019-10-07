godziny = input("Ile godzin jesteś w stanie poświęcić na naukę w tygodniu? \n")
x = 75 / int(godziny)
print("Zatem zajmie Ci to:" , x , "tygodni.")
print("W zaokrągleniu w górę:", round(x, 0) , "tygodni")