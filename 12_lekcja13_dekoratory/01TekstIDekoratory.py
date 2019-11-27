# Utwórz dekorator @uppercase_decorator,
# który przyjmuje dowolną funkcję zawracającą łańcuch znaków
# i zwracający ten sam tekst zmieniony na wielkie litery.

def simple_deco(funct):
    def nested_into_upper():
        txt = funct()

        upper_text = txt.upper()
        return upper_text
    return nested_into_upper

@simple_deco
def text_giver():
    return "It's just a piece of information."

print(text_giver())