#zapoznawanie się z klasami, obiektami

import random


class Dog:
    tail = True

    def __init__(self, name, breed, age, color, character):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.character = character
        self.pseudo = name + "-" + color

    def intelligence(self):
        IQ = ["stupid", "smart", "intelligent", "talented", "bratty"]
        return self.name + " - " + random.choice(IQ)

    def bark(self):
        return "woof " * self.age

    def tail_wave(self):
        return self.name + " is in a " + self.character + " mood so he waves it's tail!"


obj_dora = Dog("Dora", "Schnauzer", 13, "grey", "friendly")
obj_reks = Dog("Reks","Bulldog", 5, "white", "aggressive")
obj_courage = Dog("Courage", "mix", 2, "pink", "shy")
obj_scooby = Dog("ScoobyDoo", "GermanDog", 6, "brown-black", "inquisitive")
obj_lassie = Dog("Lassie", "Collie", 7, "white-brown", "brave")
obj_lajka = Dog("Łajka", "mix", 4, "white-black", "obedient")
obj_dzuma = Dog("Dżuma", "Dachshund", 2, "brown", "cheerful")
obj_bolt = Dog("Bolt", "mix", 1, "white", "brave")
obj_kiel = Dog("Biały kieł", "Husky", 5, "white-gray", "loyal")
obj_alex = Dog("Komisarz Alex", "German shepherd", 6, "brown", "brave")
obj_filip = Dog("Filipek", "York", 3, "beige", "friendly")

print(obj_dora.pseudo)
print(obj_lajka.tail)
print(Dog.tail)
print("\n")
print(obj_lassie.__dict__)
print(Dog.__dict__)
print("\n")
print(obj_lassie.intelligence())
print(Dog.intelligence(obj_dora))

names = "Anna, Marta, Paweł, Jarek, Zosia, Agnieszka"
print(names.split(","))
print(str.split(names))
print(obj_alex.bark())

print('Best doggo named {} is {}!'.format(obj_lajka.name.capitalize(), obj_lajka.character.upper()))

print(obj_dzuma.tail_wave())