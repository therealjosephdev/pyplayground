# A while loop repeats a block of code as long as a given condition is True
# When the condition becomes False, the loop stops

# name = input("Enter your name: ")

# if name == "":
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}")

#
# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# else:
#     print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old")

#
# food = input("Enter your favorite food (q to quit): ")

# while not food == "q":
#      print(f"you like {food}")
#      food = input("Enter your another favorite food (q to quit): ")
# print("bye")

# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))
# print(f"your number is {num}")

#
total_sum = 0

while True:
    user_input = input("Enter a number (or type 'done' to finish): ")
    
    if user_input.lower() == "done":
     break

    try:
       number = int(user_input)
       total_sum += number
    except ValueError:
       print("Please enter a valid number")

print(f"The total sum is {total_sum}")