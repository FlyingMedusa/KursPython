def add_book(dict_books):
    counter = int(input("Ile książek chcesz dodać: "))
    for i in range(counter):
        title = input("Podaj tytuł książki: ")
        grade = input("Podaj ocenę: ")
        dict_books[title] = grade
    return dict_books

def read_book_by_grade()

books = {}
books = add_book(books)
print(books)
g = input("Podaj ocenę książki jaką chcesz znaleźć: ")
if g in books.values():
    for title, grade in books.items():
        if grade ==g:
            print(title, "- ocena:", grade)
else:
    print("nie ma takiej książki o takiej ocenie")

print("*" * 8)

