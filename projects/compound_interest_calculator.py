# Python compound interest calculator

# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("The principle amount must be greater than zero. Please try again.")
        
# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest rate can't be less than or equal to zero")
        
# while time <= 0:
#     time = int(input("Enter the time in whole years (no decimals): "))
#     if time <= 0:
#         print("Time can't be less than or equal to zero")
        
# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time} year/s: ${total:.2f}")

#
# principle = 0
# rate = 0
# time = 0

# while True:
#     principle = float(input("Enter the principle amount: "))
#     if principle < 0:
#         print("The principle amount must be greater than zero. Please try again.")
#     else:
#         break
        
# while True:
#     rate = float(input("Enter the interest rate: "))
#     if rate < 0:
#         print("Interest rate can't be less than or equal to zero")
#     else:
#         break
        
# while True:
#     time = int(input("Enter the time in whole years (no decimals): "))
#     if time < 0:
#         print("Time can't be less than or equal to zero")
#     else:
#         break
        
# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time} year/s: ${total:.2f}")