#Day2: Anagram

#"I am Lord Voldemort" is an anagram of the character's birth name, "Tom Marvolo Riddle"

def prepare_el(word):
    word = word.lower()
    word = word.replace(" ","")
    w_sort = ''.join(sorted(word))
    return w_sort

def anagram(f_el, s_el):
    w_len = len(f_el)
    i = 0
    while i < w_len:
        elem = f_el[i]
        if f_el == s_el:
            return True
        elif elem in s_el:
            f_el = f_el.replace(elem, "")
            s_el = s_el.replace(elem, "")
        else:
            return False
        w_len = len(f_el)
        i += 1

first_el = input("Please give me the first element: \n\t")
second_el = input("Please give me the second element: \n\t")

first_el_sort = prepare_el(first_el)
second_el_sort = prepare_el(second_el)

if anagram(first_el_sort, second_el_sort):
    print("It's an anagram!")
else:
    print("Oh no! It's not an anagram!")
