
def calc_bmi(masa, wzrost):
    BMI = (float(masa)) / (float(wzrost)**2)
    return BMI

def bmi_status(BMI):
    if BMI >= 30.00:
        print("Jesteś otyły!")
        return "otylosc"
    elif BMI < 30.00 and BMI >= 25.00:
        print("Masz nadwagę!")
        return "nadwaga"
    elif BMI < 25.00 and BMI >= 18.50:
        print("Masz wagę idealną!")
        return "idealna"
    else:
        print("Masz niedowagę!")
        return "niedowaga"

def main():
    result = calc_bmi(60,1.56)
    print(bmi_status(result))

if __name__ == "__main__":
    main()