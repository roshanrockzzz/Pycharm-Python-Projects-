#Simple Command Line Temperature Conversion Program

unit = input("Is this temperature is in Celcius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9*temp)/5 + 32, 2)
    print (f"The temperture in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp-32)*5/9, 2)
    print(f"The temperture in Celcius is: {temp}°C")

else:
    print(f"{unit} is not valid")
