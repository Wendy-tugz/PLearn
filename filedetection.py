# import os
#
# path = "/Users/wendy/Documents/WEBMASTERS/PYTHON"
#
# if os.path.exists(path):
#     print("That location exits.")
#     if os.path.isfile(path):
#         print("That is a file.")
#     elif os.path.isdir(path):
#         print("That is a directory.")
# else:
#     print("That location doesn't exist.")

# Read a file

try:
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")