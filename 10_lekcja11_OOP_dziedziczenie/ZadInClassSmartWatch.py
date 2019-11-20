class Useful_stuff:

    def __init__(self):
        print("Useful stuff is sth that even you need!")

    def desc(self):
        print("Don't forget to check the battery level.")


class Watch(Useful_stuff):

    def __init__(self):
        print("Checking time with me is fast and easy.")

    def desc(self):
        super().__init__()
        super().desc()


class Phone(Useful_stuff):

    def __init__(self):
        print("Call whoever you want from wherever you are.")

    def desc(self):
        super().__init__()
        super().desc()

class Smartwatch(Watch, Phone):

    def __init__(self):
        print("I'm better than a watch! I'm better than a phone!")
        super().__init__()




u = Useful_stuff()
w = Watch()
p = Phone()
sw = Smartwatch()