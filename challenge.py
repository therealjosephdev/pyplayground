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

# Code Challenge
# Write a Python program that defines:

# A Vehicle class with attributes like brand and speed.
# A Car class that inherits from Vehicle and has an additional attribute doors.
# A Electric class that represents electric functionality (e.g., battery_life).
# A Tesla class that inherits from both Car and Electric.
# Instantiate a Tesla object and print out its details.

# Let me know if you want hints or explanations! 🚀

# class Vehicle():
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
        
#     def describe(self):
#         print(f"It is {self.brand} with a {self.speed}")

# class Car(Vehicle):
#     def __init__(self, brand, speed, doors):
#         super().__init__(brand, speed)
#         self.doors = doors

# class Electric():
#     def __init__(self, battery_life):
#         self.battery_life = battery_life

# class Tesla(Car, Electric):
#     def __init__(self, brand, speed, doors, battery_life):
#         Car.__init__(self, brand, speed, doors)
#         Electric.__init__(self, battery_life)

#     def describe(self):
#         print(f"It is a {self.brand} with a top speed of {self.speed} km/h, {self.doors} doors, and a battery life of {self.battery_life} hours.")

# tesla = Tesla(brand="Tesla", speed="250", doors=4, battery_life=500)
# tesla.describe()

# Library Management System 📚
# 💡 Project Idea: Library Management System
# A simple system where users can:
# ✅ Borrow and return books
# ✅ View available books
# ✅ Manage different types of books (e.g., E-books and Physical books)

# 🏗️ How to Structure the Code
# 🔹 Base Class: Book
# Attributes: title, author, genre
# Method: describe() (prints book details)
# 🔹 Subclasses:
# 1️⃣ PhysicalBook (inherits from Book)

# Extra attribute: shelf_location
# Overrides describe() to include shelf location
# 2️⃣ EBook (inherits from Book)

# Extra attribute: file_size
# Overrides describe() to include file size
# 🔹 Library Class
# Manages a collection of books
# Allows adding, borrowing, and returning books
# 🔹 User Class
# Can borrow and return books
# 🔹 Duck Typing:
# The borrow_book() method should work for both PhysicalBook and EBook without checking their type explicitly.

class Book():
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        
    def describe(self):
        print(f"the title is {self.title}, the author is {self.author}, the genre is {self.genre}")

class PhysicalBook(Book):
    def __init__(self, title, author, genre, shelf_location):
        super().__init__(title, author, genre)
        self.shelf_location = shelf_location
        
    def describe(self):
        super().describe()
        print(f"the shelf location is {self.shelf_location}")

class EBook(Book):
    def __init__(self, title, author, genre, file_size):
        super().__init__(title, author, genre)
        self.file_size = file_size
        
    def describe(self):
        super().describe()
        print(f"the file size is {self.file_size} MB")

class Library():
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def view_book(self):
        if not self.books:
            print("The library has no books.")
        for book in self.books:
            book.describe()

class User():
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    def borrow_book(self, library, book_title):
        for book in library.books:
            if book.title == book_title:
                self.borrowed_books.append(book)
                library.books.remove(book)
                print(f"{self.name} borrowed {book_title}")
                return  
        print(f"Sorry, {book_title} is not available in the library.")

    def return_book(self, library, book_title):
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                library.add_book(book)
                print(f"{self.name} returned {book_title}")
                return  
        print(f"{self.name} does not have {book_title}")

def main():
    library = Library()
    user = User(name=input("Enter your name: "))
    
    library.add_book(PhysicalBook("1984", "George Orwell", "Dystopian", "A1"))
    library.add_book(EBook("Python 101", "John Doe", "Programming", 5))
    
    while True:
        print("\n Library Menu")
        print("1. View Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")

        choice = input("Enter your choice: ") 

        if choice == "1":
            library.view_book()
        elif choice == "2":
            book_title = input("Enter the book title: ")
            user.borrow_book(library, book_title) 
        elif choice == "3":
            book_title = input("Enter the book title: ")
            user.return_book(library, book_title)  
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()