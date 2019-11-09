import ksztaltypomieszczen as kszpo

total_space = 0
number_of_rooms = int(input("How many rooms do you have?"))
for i in range(number_of_rooms):
    shape = input("What is the shape of your room?\n[c - circle]\n[s - square]\n[p - parallelogram]\n\t\t")
    if shape == "c":
        circle_radius = int(input("Please give the radius of your room:"))
        field = kszpo.circle_field(circle_radius)
    total_space = total_space + field
    print(total_space)