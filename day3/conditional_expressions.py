# conditional expressions = A one-line shortcut for the if-else statement (ternary operator)
#                           Print or assign one of two values based on condition
#                           X if condition else Y

#
# age = 18
# status = "Adult" if age >= 18 else "Minor"
# print(status)

#
# num = int(input("Enter a number: "))
# result = "EVEN" if num % 2 == 0 else "ODD"
# print(result)

#
# num = 5
# a = 6
# b = 7

# max_num = a if a > b else b
# min_num = a if a < b else b

# print(max_num)
# print(min_num)

#
# temp = 30

# weather = "HOT" if temp > 20 else "COLD"
# print(weather)

#
# user_role = "admin"

# access_level = "Full Access" if user_role == "admin" else "Limited Access"
# print(access_level)

# Challenge: Grade Evaluator 🎓

# score = input("what is your score: ")

# score = int(score)
# grade = "F" if score < 60 else "D" if score < 70 else "C" if score < 80 else "B" if score < 90 else "A"
# print(grade)

# Challenge: Movie Ticket Price Calculator 🎟️

# age = input("Enter your age: ")

# age = int(age)

# ticket_price = "$10" if age <= 12 else "$15" if age <= 17 else "$12" if age >= 60 else "$20"

# print(f"Your ticket price is {ticket_price}.")

# Challenge: Discount Calculator 💸

purchase_amount = float(input("Enter the purchase amount: "))

# Calculate the final price based on the discount
final_price = purchase_amount if purchase_amount < 50 else \
              purchase_amount * 0.9 if purchase_amount <= 100 else \
              purchase_amount * 0.8

print(f"The final price after discount is: ${final_price:.2f}")