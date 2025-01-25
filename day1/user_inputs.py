# input() = A function that allows user to input data
#           Returns the data entered as a string

name = input("Enter your name: ") # Enter your name:
age = int(input("Enter your age: ")) # Enter your age:

# age = int(age) # Convert age to an integer
# or you could int(age) directly in the input() function

age = age + 1 # Increment age by 1

# age = age + 1 # This will give an error because age is a string

print(f"Hello Mr {name}") # Hello Mr, name
print("HAPPY BIRTHDAY! MR", name) # HAPPY BIRTHDAY! MR name
print(f"You are {age} years old") # You are age years old