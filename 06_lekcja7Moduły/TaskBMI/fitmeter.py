import BMI as bmi


def advice(filename):
    with open(filename + ".txt") as f:
        content = f.read()
    print(content)

def main():
    masa = float(input("Podaj swoją wagę (w kilogramach): \n"))
    wzrost = float(input("Podaj swój wzrost (w metrach): \n"))
    BMI = bmi.calc_bmi(masa, wzrost)
    bmi_status = bmi.bmi_status(BMI)
    advice(bmi_status)


if __name__  == '__main__':
    main()