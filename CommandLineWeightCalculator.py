#Simple Command Line Weight Calculator
#If the input is given in Kgs it will be converted to Lbs and vice versa

weight = float(input("Enter you weight: "))
unit = input("Kilograms or Pounds? (K or P): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "P":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")

