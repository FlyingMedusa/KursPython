

class Pen:
    fruit = False
    edible = False

    def __init__(self):
        print("A pen is a writing instrument used to apply ink to a surface, usually paper.")

    def desc(self):
        return "I've got a pen!"


class Apple:
    fruit = True
    edible = True

    def __init__(self):
        print("An apple is a sweet, edible fruit produced by an apple tree.")

    def desc(self):
        return "I've got an apple!"


class Pineapple:
    fruit = True
    edible = True

    def __init__(self):
        print("The pineapple is a tropical plant with an edible fruit.")

    def desc(self):
        return "I've got pineapple!"


class Applepen(Pen, Apple):

    def __init__(self):
        print("ApplePen!")

    def desc(self):
        pen_desc = Pen.desc(self)
        app_desc = Apple.desc(self)
        print("{} {} UGH! Applepen!".format(pen_desc, app_desc))
        return "Applepen!"


class PineapplePen(Pen, Pineapple):

    def __init__(self):
        print("PineapplePen!")

    def desc(self):
        pen_desc = Pen.desc(self)
        pineapp_desc = Pineapple.desc(self)
        print("{} {} UGH! Pineapplepen!".format(pen_desc, pineapp_desc))
        return "Pineapplepen!"


class PPAP(Applepen, PineapplePen):

    def __init__(self):
        print("Penpineappleapplepen!")

    def desc(self):
        appp_desc = Applepen.desc(self)
        ppen_desc = PineapplePen.desc(self)
        print("{} {} UGH! Penpineappleapplepen!".format(appp_desc, ppen_desc))

qqq = PPAP()
qqq.desc()