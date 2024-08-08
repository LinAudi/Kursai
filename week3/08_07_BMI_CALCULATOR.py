print("BMI CALCULATOR: \n")

while True:

    def BMI(height, weight):
        result = weight / (height ** 2)
        return result

    height = float(input("Enter heigth in meters: "))
    weight = float(input("Enter weigth in kg: "))

    print(f"The BMI is : {round(BMI(height, weight), ndigits=2)}")

