# Utwórz dekorator @timepassed mierzący czas działania dowolnej funkcji.
import time
#PSEUDOKOD - TASK IN PROGRESS
start = time.now()
quicksort(lista_100000000_elementow)
snd = time.now()
timer_q = end - start

start = time.now()
countingsort(lista_10000000000000_elementow)
end = time.now()


start
bubblesort()
end

# zamiast tego robimy dekorator

def timer(sort_metod):
    def sort_elements():
        start = time.now
        sort_method()
        end = time.now()
        return end - start
    return sort_elements



clock = timer()
result_for_bubblesort = clock(bubblesort())

# a zapisuje sie to ktocej

@timer
def quicksort():
    pass

@timer
def countringsort():
    pass

@timer
def bubblesort():
    pass