class Horse:

    def give_voice(self):
        print("happy neigh")

    def fly(self):
        print("Horse can't fly")


class Unicorn:

    def give_voice(self):
        print("Rainboooowww")

    def fly(self):
        print("Unicorn can fly with magical power")



def family_test(animal):
    animal.give_voice()


arrow = Horse()
cute = Unicorn()

family_test(cute)
family_test(arrow)