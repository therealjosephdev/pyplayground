# format specifiers = {:flags} format a value based on what
#                              flags are passed to it

# .(number)f = round to that many decimal places (default 6)
# :(number) = allocate that many spaces for the value
# :03 = allocate 3 spaces for the value, pad with 0s
# :< = left align the value
# :> = right align the value
# :^ = center align the value
# :+ = show the sign of the value
# := = show a space for the sign of the value
# : = insert a space before positive numbers
# :, comma separator for large numbers

#
# price1 = 3300.13124
# price2 = -9870.45
# price3 = 1200.21

# print(f"price 1 is ${price1:+,.2f}")
# print(f"price 2 is ${price2:+,.2f}")
# print(f"price 3 is ${price3:+,.2f}")

# Challenge: Product Price Formatter 💵
product = input("Product Name: ")
quantity = float(input("Quantity: "))
unit_price = float(input("Unit Price: "))

total = unit_price * quantity

print(f"Product Name: {product}")
print(f"Quantity: {int(quantity) if quantity.is_integer() else quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Total Price: ${total:.2f}")