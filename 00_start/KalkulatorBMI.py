print("Oto minimalistyczny kalkulator BMI. \n"
      "Zaraz zostaniesz poproszony o podanie swojej wagi w kilogramach oraz wzrostu w metrach. ")
print("Pamiętaj aby podając wzrost używać kropki a nie przecinka.")
input("Jeśli jesteś gotowy wciśnij ENTER...")
masa = float(input("Podaj swoją wagę (w kilogramach): \n"))
wzrost = input("Podaj swój wzrost (w metrach): \n")
print("Zatem ważysz", masa,"kg i masz", wzrost, "m wzrostu")
BMI = (float(masa)) / (float(wzrost)**2)
print("Zgodnie z tym danymi Twoje BMI wynosi:", BMI)
