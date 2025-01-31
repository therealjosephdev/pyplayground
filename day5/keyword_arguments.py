# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")
    
# hello("Hello", "Mr.", "Joseph", "Reese")

#
# for x in range(1, 11):
#     print(x, end=" ")

#
# print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, first, last):
    return f"{country}-{first}-{last}"

phone_num = get_phone(country=20, first=9164, last=5099)

print(phone_num)