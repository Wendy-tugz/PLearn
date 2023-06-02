# functions = a block of code which is executed only when it is called.

# def hello(first_name, last_name, age):
#     print("hello! " + first_name + " " + last_name)
#     print("You are " + str(age) + " " + "years old")
#     print("Have a nice day!")
#
# hello("Wendy", "Code", 21)



# return statement

# def multiply(number1, number2):
#     return number1 * number2
#
# x = multiply(6, 8)
# print(x)

# keyword arguments


# def hello(first, middle, last):
#     print("Hello " + first + " " + middle + " " + last)
#
#
# hello(last="Code", middle="Angel", first="Wendy")

# nested function calls = function calls inside other function calls

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("Enter a whole positive number: ")))))

# scope of varibles
# Local, Enclosing, Global, Built-in variables

# name = "Bro"
# def display_name():
#     name = "Wendy"
#     print(name)
#
# display_name()
# print(name)

# args
# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#     return sum
#
#
# print(add(1, 2, 3, 4, 5))

#kwargs = parameter will pack all arguments into a dictionary

def hello(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title ="Ms.", first="Wendy", middle ="Angel", last="Code")



