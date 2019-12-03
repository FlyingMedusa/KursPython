def ordered_list(line):
    line = line.lstrip("\t")
    line = line.lstrip(" ")
    for el in line:
        if el.isnumeric():
            line = line[1:]
        elif el == ".":
            return line


# def giving_numbers(prev, line):
#     line = line.lstrip("\t")
#     line = line.lstrip("<li>")
#     prev = prev.lstrip("\t")
#     prev = prev.lstrip("<li>")
#     for i in range(0,len(prev)):
#     try:
#         elem = int(prev[i])
#         print(elem)
#     except :
#         print("not a number")
#
#     for elem in prev:
#
#         if elem.isdecimal():
#             num = elem
#         number = num



list = [" 1. I just love <b>bold text</b>." ,
        " 2. I just love <em>italic text</em>.",
        " 22. I just love <b>bold text</b>.",
        " 28. I just love <em>italic text</em>.",
        " 3. Love<b>is</b> bold."]
sentence = ". I just love <em>italic text</em>."

for line in list:
    line = line.lstrip("\t")
    line = line.lstrip("<li>")
    line = line.lstrip(" ")
    number = ""
    for i in range(0, len(line)):
        try:
            elem = int(line[i])
            number = number + str(elem)
        except:
            break

    number = int(number)

    new_number = number + 1
    print(new_number)
    sentence = str(new_number) + sentence
    print(sentence)



