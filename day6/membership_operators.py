# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

# students = {"Spongebob", "Patrick", "Sandy"}

# student = input("Enter the name of a student: ").capitalize()

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")

# grades = {"Sandy": "A",
#           "Squidward": "B",
#           "Spongebob": "C",
#           "patrick": "D"}

# student = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

email = "JospehReese@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")