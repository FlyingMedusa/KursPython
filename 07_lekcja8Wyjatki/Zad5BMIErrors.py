
def calc_bmi(masa, wzrost):
    BMI = (float(masa)) / (float(wzrost)**2)
    return BMI

def bmi_status(BMI):
    if BMI >= 30.00:
        print("Jesteś otyły!")
    elif BMI < 30.00 and BMI >= 25.00:
        print("Masz nadwagę!")
    elif BMI < 25.00 and BMI >= 18.50:
        print("Masz wagę idealną!")
    else:
        print("Masz niedowagę!")

print("Oto minimalistyczny kalkulator BMI. \nZaraz zostaniesz poproszony o podanie swojej wagi w kilogramach oraz wzrostu w metrach. ")
print("Pamiętaj aby podając wzrost używać kropki a nie przecinka.")
input("Jeśli jesteś gotowy wciśnij ENTER...")

try:
    masa = float(input("Podaj swoją wagę (w kilogramach): \n"))
except ValueError as e:
    print("Podej tylko liczbową wartość Twej wagi")


try:
    wzrost = float(input("Podaj swój wzrost (w metrach): \n"))
except ValueError as e:
    print("Podej tylko liczbową wartość Twego wzrostu")

print("Zatem ważysz", masa,"kg i masz", wzrost, "m wzrostu")

BMI = calc_bmi(masa, wzrost)
print("Zgodnie z tym danymi Twoje BMI wynosi:", BMI)
bmi_status(BMI)


