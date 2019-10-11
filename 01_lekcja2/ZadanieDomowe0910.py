#Zadanie drugie
print("Zadanie drugie: wsadzanie zdania s2 w zdanie s1 \n")
s1 = input("Podaj pierwsze zdanie: \n")
s2 = input("Podaj drugie zdanie: \n")
middle = len(s1)//2
print(s1[:middle] +s2 + s1[middle:])

#Zadanie czwarte
print("Zadanie czwarte:")
print("Sprawdzę czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową \n ")
title = input("Podaj tytuł: \n")
surname = input("Podaj nazwisko autora: \n")
pages = input("Podaj ilość stron: \n")
print(title.isalpha() , surname.isalpha() , pages.isdigit())
print("Pilnuję by tytuły i nazwiska były z dużej litery:")
print(title.capitalize())
print(surname.capitalize())
print(" Podaję dane jednym ciągiem ze spacjami: ")
book = title.capitalize() + " " + surname.capitalize() + " " + pages
print(book)
print("Liczę liczbę znaków w ciągu 'book'")
print(len(book))

#Zadanie 6
zenpython = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
print(zenpython.count("better"))