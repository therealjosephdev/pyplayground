# function = A block of reusable code
#            place () after the function name to invoke it


# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()
    
# happy_birthday("Joseph", 20)
# happy_birthday("Reese", 30)
# happy_birthday("Steve", 40)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
    
# display_invoice("JosephReese", 100.25, "01/01")

# return = statement used to end a function
#          and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))

#
# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# full_name = create_name("joseph", "reese")
# print(full_name)

# Employee Salary Calculator 💰

# def calculate_salary():
#     hourly_wage = float(input("Enter hourly wage: "))
#     hours_worked = float(input("Enter hours worked: "))
#     return hourly_wage * hours_worked

# print(f"Total salary: {calculate_salary():.2f}")

# improved

# def calculate_salary(hourly_wage, hours_worked):
#     return hourly_wage * hours_worked

# hourly_wage = float(input("Enter hourly wage: "))
# hours_worked = float(input("Enter hours worked: "))

# total_salary = calculate_salary(hourly_wage, hours_worked)
# print(f"Total salary: ${total_salary:.2f}")

# Student Grade Calculator 🎓

# def calculate_grade(first, second, third):
#     return (first + second + third) / 3

# first_exam = float(input("Enter first exam score: "))
# second_exam = float(input("Enter second exam score: "))
# third_exam =  float(input("Enter third exam score: "))

# score = calculate_grade(first_exam, second_exam, third_exam)

# print(f"average score: {score:.2f}")

# grade = "F" if score < 60 else "D" if score < 70 else "C" if score < 80 else "B" if score < 90 else "A"

# print(f"Final Grade: {grade}")