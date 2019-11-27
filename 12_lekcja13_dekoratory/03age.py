#funkcja, która zwraca wiek osoby i dekorator który zwraca pełnoletni i niepełnoletni

def age_deco(age):
    def nested_age():
        user_age = age()

        if user_age > 18:
            return "adult"
        else:
            return "kid"
    return nested_age

@age_deco
def paula():
    age = 18
    return age

@age_deco
def tosia():
    age = 21
    return age

print(paula())
print(tosia())