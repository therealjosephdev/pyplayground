# prints

# name = "Joseph Reese"

# print(f"Hello, {name}!")

# quote = "the quote goes like this one day or day one one day\nor day one uh I'll do it one day okay, that's up to you or day\none this is day one."

# print(quote)

# Task = "Learn Python\nExercise\nWatch TV"
# Priority = "High\nMedium\nLow"

# print("Task\t\t| Priority")
# print("------------------------")
# print("Learn Python\t| High")
# print("Exercise\t| Medium")
# print("Watch TV\t| Low")

# variables

# name = "Joseph Reese"
# age = 17
# favorite_number = 7

# print(f"My name is {name} I'm {age} years old, and my favorite number is {favorite_number}.")

# first_name = "Joseph"
# last_name = "Reese"

# first_name, last_name = last_name, first_name

# print(f"My first name is {first_name} and my last name is {last_name}.")

# User Inputs

# age = int(input("Enter your age: "))
# height = float(input("Enter your height (in centimeters): "))

# # Convert height to meters
# height_in_meters = height / 100

# print(f"You are {age} years old and {height_in_meters:.2f} meters tall.")

# Type Casting

# age = input("Enter your age: ")
# height = input("Enter your height (in centimeters): ")

# age = int(age)
# height = float(height)

# Convert height to centimeters
# height_in_feet = height / 30.48

# age_in_months = age * 12

# print(f"You are {age_in_months} months old and {height_in_feet:.2f} feet tall.")

# everything learned in day one

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# age = int(input("Enter your age: "))
# height = input("Enter your height (in centimeters): ")

# age_in_months = age * 12
# height_in_meters = float(height) / 100

# print(f"Your name is {first_name} {last_name}. You are {age_in_months} months old and {height_in_meters:.2f} meters tall.")

#Challenge: Admission Checker 🎟️
# valid_inputs = ["Y", "N"]

# age = input("How old are you? : ")
# try:
#     age = float(age)
#     if age < 18:
#         print("Sorry, you're too young to enter.")
#     else:
#         vip_ticket = input("Do you have a VIP ticket? (Y/N): ").strip().upper()
#         if vip_ticket not in valid_inputs:
#             print("Invalid input. Please enter 'Y' or 'N'.")
#         elif vip_ticket == "Y":
#             print("Welcome to the concert!")
#         else:
#             standard_ticket = input("Do you have a STANDARD ticket? (Y/N): ").strip().upper()
#             if standard_ticket not in valid_inputs:
#                 print("Invalid input. Please enter 'Y' or 'N'.")
#             elif standard_ticket == "Y":
#                 print("Welcome to the concert!")
#             else:
#                 print("Sorry, you need a ticket to enter.")
# except ValueError:
#     print("Invalid age. Please enter a number.")

# Challenge: Scholarship Eligibility Checker 🎓
# valid_inputs = ["Y", "N"]

# gpa = float(input("Enter your GPA: "))
# volunteer_hours = int(input("Enter your volunteer hours: "))
# recommendation_letter = input("Do you have a recommendation letter? (Y/N): ").strip().upper()

# if gpa >= 3.5 and (volunteer_hours >= 500 or recommendation_letter == "Y"):
#     print("You are eligible for the scholarship!")
# else:
#     print("You are not eligible for the scholarship.")

# # Movie Ticket Price Calculator 🎥

# # Get user inputs
# age = int(input("Enter your age: "))
# snack_combo = input("Do you want a snack combo (Y/N): ").strip().upper()

# # Determine the ticket price based on age
# if age < 12:
#     ticket_price = 10
# elif 12 <= age <= 59:
#     ticket_price = 15
# else:  # Seniors aged 60 and above
#     ticket_price = 12

# # Add the cost of a snack combo if selected
# if snack_combo == "Y":
#     ticket_price += 5

# # Output the final ticket price
# print(f"The total price for your ticket is ${ticket_price:.2f}")

# Challenge: Gym Membership Cost Calculator 🏋️‍♀️

# age = float(input("Enter your age: "))
# premium_plan = input("Do you want the premium plan (Y/N): ").strip().upper()

# if age < 18:
#     membership_price = 20
# elif 18 <= age <= 60:
#     membership_price = 40
# else:
#     membership_price = 30

# if premium_plan == "Y":
#     membership_price += 15

# print(f"Your monthly membership cost is ${membership_price:.2f}.")
