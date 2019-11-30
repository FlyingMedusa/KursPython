# Utwórz klasę sklep. Sklep posiada różne produkty.
# W sklepie można produkt zobaczyc, przymierzyc, kupic, zwrocic.
import random


class Shop:
    vat = 0.23
    emotion = ["amazed", "disappointed", "enchanted", "charmed", "bummed", "disgusted"]

    def __init__(self, item, type, color, price, discount):
        self.item = item
        self.type = type
        self.color = color
        self.price = price
        self.discount = discount

    def __repr__(self):
        return self.item.upper()

    # def display(self, array):
    #     self.array = array
    #     for i in array:
    #         print(array[i])




    @property
    def item_ID(self):
        disc = self.discount
        disc = disc.replace("%","")
        return '{} ID: 00-{}-{}-32'.format(self.item, self.price, disc)


class Clothes(Shop):

    def look_on(self):
        reasons = ["the amount of sequins", "the bright color", "how expensive it is", "how cheap it is"]
        print("You look at " + self.item + " and you're " + random.choice(self.emotion) + " by " + random.choice(
            reasons) + ".")

    def try_on(self):
        appearance = ["stylish", "good", "bad", "fat", "stunning", "obese"]
        print("You try " + self.item + " on and you look " + random.choice(appearance) + "!")


class Jewellery(Shop):

    def look_on(self):
        reasons = ["how expensive it is", "how cheap it is", "how rare it is", "how downscale it is"]
        print("You look at " + self.item + " and you're " + random.choice(self.emotion) + " by " + random.choice(
            reasons) + ".")

    def try_on(self):
        appearance = ["stylish", "good", "bad", "stunning", "rich", "like Kim Kardashian"]
        print("You try " + self.item + " on and you look " + random.choice(appearance) + "!")


class Cosmetics(Shop):

    def look_on(self):
        reasons = ["how expensive it is", "how cheap it is", "how low-quality it is", "the nice box design"]
        print("You look at " + self.item + " and you're " + random.choice(self.emotion) + " by " + random.choice(
            reasons) + ".")



it_dress = Clothes("party dress", "clothes", "red", 120, "20%")
it_shoes = Clothes("casual shoe", "clothes", "brown", 240, "10%")
it_heels = Clothes("high heel", "clothes", "black", 220, "5%")
it_hat = Clothes("elegant hat", "clothes", "black", 80, "20%")
it_necklace = Jewellery("golden necklace", "jewellery", "gold", 560, "5%")
it_earrings = Jewellery("long earring", "jewellery", "sliver", 150, "10%")
it_ring = Jewellery("diamond ring", "jewellery", "silver", 1250, "0%")
it_coat = Clothes("warm coat", "clothes", "black", 360, "20%")
it_mascara = Cosmetics("blue mascara", "cosmetics", "blue", 25, "30%")
it_lashes = Cosmetics("fake lashes", "cosmetics", "brown", 50, "0%")
it_lipstick = Cosmetics("crimson lipstick", "cosmetics", "crimson", 80, "25%")

arr_shop = [it_dress, it_shoes, it_heels, it_hat, it_necklace, it_earrings, it_ring, it_coat, it_mascara, it_lashes, it_lipstick]

# print(Shop.display(arr_shop))
it_ring.try_on()
it_shoes.look_on()
it_necklace.look_on()
print(it_necklace)
print(it_earrings.item_ID)