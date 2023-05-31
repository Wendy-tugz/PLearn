import time

name = "Bro Code"

# print(len(name))
# print(name.find("C"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o", "a"))
# print(name*4)

# type casting = converting a data type of a value to another data type

# x = 1
# y = 2.0
# z = "3"

# x = str(x)
# y = str(y)
# z = str(z)

# print("X is " + str(x))
# print("Y is " + str(y))
# print(z*3)

# slicing
# name = "Wendy Code"
# first_name = name[:5]
# last_name = name[6:]
# reversed_name = name[::-1]
#
# print(first_name)
# print(last_name)
# print(reversed_name)

# website = "http://google.com"
# slice = slice(7,-4)
# print(website[slice])

# If statment

# If
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()


# loop control statements
# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)