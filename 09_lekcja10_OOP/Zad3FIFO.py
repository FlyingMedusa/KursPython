# Stwórz własną implementację kolejki FIFO.
# Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta,
# dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).


class Fifo:

    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        return " - ".join(self.elements)

    def show(self):
        print(self.elements)


    def put(self):
        el = input("Give me an element: ")
        self.elements.append(el)
        return self.elements

    def get(self):
        if len(self.elements) == 0:
            return "no elements"
        else:
            return self.elements.pop(0)




list_elem = ["a", "b", "c", "d"]
fifo = Fifo(list_elem)

print(fifo)
fifo.show()
fifo.put()
print(fifo.elements)
print(fifo.get())
print(fifo.get())
print(fifo.get())
print(fifo.get())
print(fifo.get())
