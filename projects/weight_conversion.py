# Python Weight conversion

#
# valid_uints = ["kg", "lbs"]

# uint = input("Enter the unit (kg, lbs): ")
# if uint not in valid_uints:
#     print("Invalid uint. Please use kg, lbs")
# else:
#     weight = float(input("Please enter your weight: "))

# if uint =="kg":
#     print(f"your weight in pounds is {weight * 2.205}")
# elif uint =="lbs":
#     print(f"your weight in kilograms is {weight / 2.205}")

#
# valid_units = ["kg", "lbs"]

# unit = input("Enter the unit (kg, lbs): ").lower()
# if unit not in valid_units:
#     print("Invalid unit. Please use 'kg' or 'lbs'.")
# else:
#     try:
#         weight = float(input("Please enter your weight: "))
#         if unit == "kg":
#             print(f"Your weight in pounds is {weight * 2.205:.2f}")
#         elif unit == "lbs":
#             print(f"Your weight in kilograms is {weight / 2.205:.2f}")
#     except ValueError:
#         print("Invalid weight. Please enter a number.")

# BRO CODE
# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K or L): ")

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs."
#     print(f"Your weight is: {round(weight, 1)} {unit}")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs."
#     print(f"Your weight is: {round(weight, 1)} {unit}")
# else:
#     print(f"{unit} was not vaild")

