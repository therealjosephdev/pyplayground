# Python Temperature conversion

valid_units = ["C", "F"]

unit = input("Enter the unit (C, F): ").upper()
if unit not in valid_units:
    print("Enter 'C' for Celsius or 'F' for Fahrenheit.")

else:
    try:
        temperature = float(input("Enter the temperature: "))
        if unit == "C":
            print(f"{temperature}°C is equivalent to {temperature * 9 / 5 + 32}°F")
        elif unit == "F":
            print(f"{temperature}°F is equivalent to {(temperature - 32) * 5 / 9}°C")
    except ValueError:
        print("Invalid temperature. Please enter a number.")