# Python reading files (.txt, .json, .csv)

# file_path = "output.txt"

# try:
#     with open(file_path, "r") as file:
#         output = file.read()
#         print(output)
# except FileNotFoundError:
#     print(f"File is not found!")
# except PermissionError:
#     print("Permission is needed to read the file!")

# JSON

# import json

# file_path = "output.json"

# try:
#     with open(file_path, "r") as file:
#         output = json.load(file)
#         print(output["name"])
# except FileNotFoundError:
#     print(f"File is not found!")
# except PermissionError:
#     print("Permission is needed to read the file!")

# CSV

# import csv

# file_path = "output.csv"

# try:
#     with open(file_path, "r") as file:
#         output = csv.reader(file)
#         for line in output:
#             print(line[0])
# except FileNotFoundError:
#     print(f"File is not found!")
# except PermissionError:
#     print("Permission is needed to read the file!")