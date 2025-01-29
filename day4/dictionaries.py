# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

# capitals = {"USA": "Washington D.C.",
#             "India": "New Delhi",
#             "Russia": "Moscow",
#             "EGYPT": "Cairo"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))

# if capitals.get("EGYPT"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exit")
    
# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("India")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)

# values = capitals.values()

# for value in capitals.values():
#     print(value)
    
# items = capitals.items()

# for key, value in capitals.items():
#     print(f"{key}: {value}")
    
#    
# Write a dictionary that represents a book with the following information:

# Title: "Python Basics"
# Author: "John Doe"
# Year: 2021
# Write code to retrieve the value of the "Author" key from the above dictionary.

# Write code to add a new key "Pages" with the value 350 to the dictionary you created in Question 5.

# How can you check if a key (e.g., "Year") exists in a dictionary?

# book = {
#     "Title": "Python Basics",
#     "Author": "John Doe",
#     "Year": 2021
# }

# print(book.get("Author"))

# book.update({"Pages": 350})

# if "Year" in book:
#     print("exists")
# else:
#     print("doesn't exist")

# Challenge: Student Grades Tracker

# grades = {}

# while True:
#     alice = float(input("Enter Alice's grade: "))
#     bob = float(input("Enter Bob's grade: "))
#     charlie = float(input("Enter Charlie's grade: "))
    
#     grades['Alice'] = alice
#     grades['Bob'] = bob
#     grades['Charlie'] = charlie
    
#     break

# for key, value in grades.items():
#     print(f"{key}: {value}")
    
# average = (bob + alice + charlie) / 3
# print(f"The average is: {average:.2f}")

# BETTER

grades = {}

while True:
    try:
        alice = float(input("Enter Alice's grade: "))
        if alice < 0 or alice > 100:
            print("Grade must be between 0 and 100.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    try:
        bob = float(input("Enter Bob's grade: "))
        if bob < 0 or bob > 100:
            print("Grade must be between 0 and 100.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
        
    try:
        charlie = float(input("Enter Charlie's grade: "))
        if charlie < 0 or charlie > 100:
            print("Grade must be between 0 and 100.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    grades['Alice'] = alice
    grades['Bob'] = bob
    grades['Charlie'] = charlie
    break

for key, value in grades.items():
    print(f"{key}: {value}")

average = (bob + alice + charlie) / 3
print(f"The average is: {average:.2f}")

 