# concession stand program 🍿

menu = {"Popcorn": 5.00,
         "Soda": 3.25,
         "Nachos": 6.50,
         "Candy": 2.00
}

cart = []
total = 0

print("Welcome to the Concession Stand 🍿!")
print("---------------- MENU -------------------")

for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
    
while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif food.capitalize() in menu:
        cart.append(food.capitalize())

print("---------------- YOUR ORDER -------------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
    
print()
print(f"Total is: {total:2f}")