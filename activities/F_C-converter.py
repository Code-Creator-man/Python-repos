unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (9 * temp) / 5 + 32
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = (temp - 32) * 5 / 9
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is invalid unit of measurement")