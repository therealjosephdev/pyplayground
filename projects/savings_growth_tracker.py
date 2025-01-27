# Challenge: Savings Growth Tracker 💰

initial_deposit = 0
monthly_contribution = 0
apr = 0
time = 0

while True:
    initial_deposit = float(input("Enter the initial deposit: "))
    if initial_deposit <= 0:
        print("The initial deposit amount must be greater than zero. Please try again.")
    else:
        break

while True:
    monthly_contribution = float(input("Enter the monthly contribution: "))
    if monthly_contribution <= 0:
        print("Monthly contribution can't be less than or equal to zero")
    else:
        break

while True:
    apr = float(input("Enter the annual interest rate (in %): "))
    if apr <= 0:
        print("Annual interest rate can't be less than or equal to zero")
    else:
        break
    
while True:
    time = int(input("Enter the time in whole years (no decimals): "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break

r = apr / 100
n = 12
    
total_from_initial = initial_deposit * pow(1 + r / n, n * time)
total_from_contributions = monthly_contribution * ((pow(1 + r / n, n * time) - 1) / (r / n))

total = total_from_initial + total_from_contributions

print(f"Balance after {time} year(s): ${total:.2f}")