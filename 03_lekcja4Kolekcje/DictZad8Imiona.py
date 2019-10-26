#Słowniki dla 10 krajów Europy utwórz listy 10 najpopularniejszych imion żeńskich.
# Za każdym razem zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem.
# Nowa lista powinna zawierać 100 elementów.
#Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

country_names = {
    "UK":["Olivia", "Sophia", "Lily", "Ava", "Mia", "Isla", "Amelia", "Freya", "Isabella", "Emily"],
    "USA":["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Charlotte", "Mia", "Amelia", "Harper", "Evelyn"],
    "Australia": ["Charlotte", "Olivia", "Ava", "Amelia", "Mia", "Isla", "Grace", "Ella", "Chloe", "Harper"],
    "Canada": ["Olivia", "Emma", "Charlotte", "Sophia", "Aria", "Ava", "Chloe", "Zoey", "Abigail", "Amelia"],
    "Ireland": ["Emily", "Grace", "Emma", "Sophie", "Amelia", "Ella", "Ellie", "Mia", "Ava", "Fiadh"],
    "New Zealand": ["Charlotte", "Isla", "Olivia", "Amelia", "Ella", "Harper", "Isabella", "Emily", "Mia", "Ava"],
    "Jamaica": ["Selena", "Gabriel", "Danielle", "Kristen", "Shanice", "Britney", "Jessica", "Tara", "Alyssa", "Victoria"],
    "Dominica": ["Lola", "Maria", "Diana", "Fleur", "Sarah", "Jenniffer", "Andrea", "Elena", "Janerin", "Genesis"],
    "Bahamas": ["Marifer", "Galy", "Sabrina", "Kate", "Tamasha", "Ledeja", "Emma", "Marge", "Isabella", "Samara"],
    "Barbados": ["Tiana", "Jenna", "Carolyn", "Rebecca", "Adanna", "Erica", "Patricia", "Kaylia", "Shannon", "Tiarra"]
}

names_dict = {}

for country, names_list in country_names.items():
    for name in names_list:
        if name in names_dict:
            names_dict[name] += 1
        else:
            names_dict[name] = 1

for name, count in names_dict.items():
    if count > 2:
        print(name, "-", count)



