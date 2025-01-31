# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is Wednesday"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _:
#             return "Not a valid day"
        
# print(day_of_week(1))

# def is_weekend(day):
#     match day:
#         case "Sunday":
#             return True
#         case "Monday":
#             return False
#         case "Tuesday":
#             return False
#         case "Wednesday":
#             return False
#         case "Thursday":
#             return False
#         case "Friday":
#             return False
#         case "Saturday":
#             return True
#         case _:
#             return False
        
# print(is_weekend("Saturday"))

# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return False
#         case _:
#             return False
        
# print(is_weekend("Monday"))

#

# print("Welcome to the Vending Machine!")
# print("1. Coke - $1.50")
# print("2. Water - $1.00")
# print("3. Juice - $2.00")

# while True:
#     choice = input("Enter your choice: ").strip().lower()
#     if choice == "1":
#         print("You selected Coke. That will be $1.50.")
#         break
#     elif choice == "2":
#         print("You selected Water. That will be $1.00.")
#         break
#     elif choice == "3":
#         print("You selected Juice. That will be $2.00.")
#         break
#     else:
#         print("invalid choice.")

#
print("Welcome to the Vending Machine!")
print("1. Coke - $1.50")
print("2. Water - $1.00")
print("3. Juice - $2.00")

def vending_machine():
    choice = input("Enter your choice: ").strip()
    match choice:
        case "1":
            return "You selected Coke. That will be $1.50."
        case "2":
            return "You selected Water. That will be $1.00."
        case "3":
            return "You selected Juice. That will be $2.00."
        case _:
            return "Invalid choice, please try again!"

print(vending_machine())