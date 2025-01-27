# string methods in python

# name = input("Enter your full name: ")

# result = len(name)

# print(result)

#
# name = input("Enter your full name: ")

# result = name.find("j")

# print(result)

#
# if python can't find the letter it will return -1
# name = input("Enter your full name: ")

# result = name.rfind("j")

# print(result)

#
# name = input("Enter your full name: ")
# result = name.capitalize()
# print(result)

# make all letters uppercase
# name = input("Enter your full name: ")
# name = name.upper()
# print(name)

# make all letters lowercase
# name = input("Enter your full name: ")
# name = name.lower()
# print(name)

#
# name = input("Enter your full name: ")
# result = name.isdigit()
# print(result)

#
# name = input("Enter your full name: ")
# result = name.isalpha()
# print(result)

#
# phone_number = input("Enter your phone #: ")
# result = phone_number.count("-")
# print(result)

#
# phone_number = input("Enter your phone #: ")
# phone_number = phone_number.replace("-", "")
# print(phone_number)

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif " " in username:
    print("Your user name can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")