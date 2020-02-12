class Mammals:
    breasts = True

    def __init__(self):
        print("Mammals are characterized by the presence of mammary glands.")

    def desc(self):
        print("Most mammals are intelligent, with some possessing large brains, self-awareness, and tool use.")


class Cat(Mammals):

    def __init__(self, name):
        print("A catto!")
        self.name = name

    def desc(self):
        super().__init__()
        super().desc()
        print("However, cats are domesticated aliens!")

    def sound(self):
        return "meow"

class Dog(Mammals):

    def __init__(self, name):
        print("A doggo!")
        self.name = name

    def desc(self):
        super().desc()
        print("Indeed, dogs are the smartest of them all!")

    def sound(self):
        return "woof woof"

class Human(Mammals):

    def __init__(self, name):
        print("Oh, just a human...")
        self.name = name

    def desc(self):
        super().desc()
        print("{} says {}!".format(human1.name, human1.sound()))
        print("Unfortunately not all human beings seem to meet those criteria...")

    def sound(self):
        return "I need more potatoes in my soup..."

print("Look what we have here!")
cat1 = Cat("Messy")
dog1 = Dog("Dora")
human1 = Human("Janusz")
print("")
cat1.desc()
print("{} says {}!\n".format(cat1.name,cat1.sound()))
dog1.desc()
print("{} says {}!\n".format(dog1.name,dog1.sound()))
human1.desc()