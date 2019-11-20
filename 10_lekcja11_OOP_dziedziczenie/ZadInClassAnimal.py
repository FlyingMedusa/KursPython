class Vertebrate:
    backbone = True

    def __init__(self):
        print("Vertebrate - an animal with a spinal cord surrounded by cartilage or bone.")

    # def __str__(self):
    #     return "I'm a vertebrate!"
    def desc(self):
        print("Vertebrates include birds, fish, amphibians, reptiles, and mammals")


class Cat(Vertebrate):

    def __init__(self, name):
        print("A kitten!")
        self.name = name

    def desc(self):
        super().__init__()
        super().desc()
        print("but cats are just domesticated aliens!")

    def sound(self):
        return "meow"



kitty = Cat("Kitty")
kitty.desc()