import random


def ran_name():
    name_length = random.randint(3, 7)
    return name_length


def even(name_length):
    name_even = name_length % 2
    if name_even == 1:
        name_length = name_length + 1
    return name_length


def name_creator():
    indicator = (name_length / 2) + 1
    i = 1
    while i < indicator:
        cons = random.choice(consonants)
        vow = random.choice(vowels)
        name.append(cons)
        name.append(vow)
        i += 1
    return name


def blind_element(array):
    element = random.choice(array)
    return element


def finding_the_killer(array):
    killer = random.choice(array)
    return killer


consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Z"]
vowels = ["A", "E", "I", "O", "U", "Y"]
name = []
alias = ["manly", "combati", "reasonable", "furious", "brave", "cunny", "fast", "old", "alluring"]
race = ["dwarf", "minotaur", "elf", "driad", "witch", "thief", "human", "troll", "gnome", "dragon", "siren"]
places = ["forest", "castle", "town", "cave", "seaside", "river", "pub", "dungeon", "king's chamber","queen's chamber"]
npcs = ["the Queen", "royal knight", "beautiful maid", "young prisoner", "your mother", "king's advisor"]
actions = ["reading books", "selling potions", "cleaning up", "eating a chicken", "looking at the sky", "writing a letter"]

name_length = ran_name()
name_length = even(name_length)
name = name_creator()


final_name = "".join(name)
final_name = final_name.capitalize()
final_alias = random.choice(alias)
final_race = random.choice(race)

warrior_name = "{name} the {alias} {race}".format(name=final_name, alias=final_alias, race=final_race)

#--------------------------------------------------------------------------------------

killer = finding_the_killer(npcs)

intro = "\nHello {name}! Your king was killed and now you need to find the killer!\nYou have only 8 days to found out who killed your king! Otherwise he will kill you too!".format(name=warrior_name)
print(intro)


i = 1
while i < 9:
    place = blind_element(places)
    person = blind_element(npcs)
    standard_plot = "\nYou go to {place} and meet there a {person} who is {action}.".format(
        place=place,
        person=person,
        action=blind_element(actions))
    print(standard_plot)
    question = input("Is that person a killer? [y/n]\n\t")
    if question == "y":
        if person == killer:
            print("You saved the city!")
            break
        else:
            print("This person is not a killer. What a shame!")
    if i == 8:
        print("8 days have passed and you're getting killed!\n\t\tTHE END")
    i += 1
