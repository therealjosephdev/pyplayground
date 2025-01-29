import random

# # low = 1
# # high = 100
# # options = ("rock", "paper", "scissors")
# # cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# # number = random.randint(low, high)
# # number = random.random()
# # option = random.choice(options)
# # random.shuffle(cards)

# # print(cards)

#
# ✏️ 1. Write a Python program to generate a random number between 50 and 100.
# ✏️ 2. Write code to pick a random item from this list:
#       colors = ["Red", "Blue", "Green", "Yellow"]
# ✏️ 3. Generate a random floating-point number between 1.5 and 6.5.

first = 50
last = 100

colors = ["Red", "Blue", "Green", "Yellow"]

number = random.randint(first, last)
print(number)

color = random.choice(colors)
print(color)

floating = random.uniform(1.5, 6.5)
print(floating)