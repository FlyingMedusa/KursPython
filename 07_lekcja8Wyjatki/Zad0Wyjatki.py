import sys

# try:
#     mak = int(input("Podaj ile maku\t"))
#     proporcje_ciasta = 12/ mak
#     print(proporcje_ciasta)
# except Exception as e:
#     print("No exception jak nic!\t", sys.exc_info()[0])
# finally:
#     print("Maku zawsze za mało!")

def predict_future():
  num = int(input("Podaj dowolną liczbę naturalną: "))
  if num < 0:
    raise ValueError("To nie jest liczba naturalna!")
  else:
    print("Za", 10 * num, "lat ludzkość będzie mogła się teleportować")

try:
  predict_future()
except ValueError as e:
    print(e)