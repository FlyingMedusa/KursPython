# Utwórz klasę sklep. Sklep posiada różne produkty.
# W sklepie można produkt zobaczyc, przymierzyc, kupic, zwrocic.
import random


class Shop:

    def __init__(self, item, type, color, price, discount):
        self.item = item
        self.type = type
        self.color = color
        self.price = price
        self.discount = discount

    def display(self):
        for i in arr_shop:
            print(i)

    def try_on(self):
        appearance = ["stylish", "good", "bad", "fat", "stunning", "obese"]
        print("You try " + self.item + " on and you look " + random.choice(appearance) + "!")

    def look_on(self):
        emotion = ["amazed", "disappointed", "enchanted", "charmed", "bummed", "disgusted"]
        if self.type == "clothes":
            reasons = ["the amount of sequins", "the bright color", "how expensive it is", "how cheap it is"]
        elif self.type == "jewellery":
            reasons = ["how expensive it is", "how cheap it is", "how rare it is", "how downscale it is"]
        elif self.type == "cosmetics":
            reasons = ["how expensive it is", "how cheap it is", "how low-quality it is", "the nice box design"]
        print("You look at " + self.item + " and you're " + random.choice(emotion) + " by " + random.choice(reasons) + ".")


it_dress = Shop("party dress", "clothes", "red", 120, "20%")
it_shoes = Shop("casual shoe", "clothes", "brown", 240, "10%")
it_heels = Shop("high heel", "clothes", "black", 220, "5%")
it_hat = Shop("elegant hat", "clothes", "black", 80, "20%")
it_necklace = Shop("golden necklace", "jewellery", "gold", 560, "5%")
it_earrings = Shop("long earring", "jewellery", "sliver", 150, "10%")
it_ring = Shop("diamond ring", "jewellery", "silver", 1250, "0%")
it_coat = Shop("warm coat", "clothes", "black", 360, "20%")
it_mascara = Shop("blue mascara", "cosmetics", "blue", 25, "30%")
it_lashes = Shop("fake lashes", "cosmetics", "brown", 50, "0%")
it_lipstick = Shop("crimson lipstick", "cosmetics", "crimson", 80, "25%")

arr_shop = [it_dress, it_shoes]

Shop.display(arr_shop)
it_mascara.try_on()
it_shoes.look_on()
it_necklace.look_on()