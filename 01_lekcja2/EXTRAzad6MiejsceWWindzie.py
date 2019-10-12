# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość. 
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy (jest to prawdopodobne)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
lod_wys = float(input("Podaj wysokość lodówki w metrach:\n \t \t"))
lod_sze = float(input("Podaj szerokość lodówki w metrach:\n \t \t"))
lod_gle = float(input("Podaj głębokość lodówki w metrach:\n \t \t"))
win_wys = float(input("Podaj wysokość windy w metrach:\n \t \t"))
win_sze = float(input("Podaj szerokość windy w metrach:\n \t \t"))
win_gle = float(input("Podaj głębokość windy w metrach:\n \t \t"))
lod_obj = lod_wys*lod_sze*lod_gle
win_obj = win_wys*win_sze*win_gle
miejsce = win_obj-lod_obj
print("W windzie pozostało", miejsce, "metrów sześciennych")