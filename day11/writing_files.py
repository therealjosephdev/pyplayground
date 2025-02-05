# Python writing files (.txt, .json, .csv)

# txt_data = "I like pizza!"

# file_path = "output.txt"

# try:
#     with open(file=file_path, mode="a") as file:
#         file.write("\n" + txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

#

# import json

# employee = {
#     "name": "John Reese",
#     "age": 40,
#     "job": "Former member of the U.S. Army Special Forces and CIA National Clandestine Service (NCS) Special Activities Division (SAD) officer"
# }

# file_path = "output.json"

# try:
#     with open(file=file_path, mode="w") as file:
#         json.dump(employee, file, indent=5)
#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

#

# import csv

# employees = [["Name", "Age", "Job"],
#              ["Spongebob", 30, "Cook"],
#              ["Patrick", 37, "Unemployed"],
#              ["Sandy", 27, "Scientist"]]

# file_path  = "output.csv"

# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")