# Wersja 1
books = {}
counter = int(input("Ile książek chcesz dodać: "))

for i in range(counter):
    title = input("Podaj tytuł książki: ")
    grade = input("Podaj ocenę: ")
    books[title] = grade

print(books)

# Wersja 2

def add_book(dict_books):
    counter = int(input("Ile książek chcesz dodać: "))
    for i in range(counter):
        title = input("Podaj tytuł książki: ")
        grade = input("Podaj ocenę: ")
        dict_books[title] = grade
    return dict_books


books = {}
books = add_book(books)
print(books)