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

# def hello(**kwargs):
#     # print("Hello " + kwargs['first'] + " " + kwargs['last'])
#     print("Hello", end=" ")
#     for key, value in kwargs.items():
#         print(value, end=" ")
#
# hello(title ="Ms.", first="Wendy", middle ="Angel", last="Code")

# str.format() method = optional method that gives users more control when displaying output

# animal = "cow"
# item = "moon"

# print("The " + animal + " " + "jumped over the " + item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item)) #positional argument
# print("The {item} jumped over the {animal}".format(animal="cow", item="moon")) #keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal, item))

# name = "Wendy"
#
# print("Hello my name is {}".format(name))
# print("Hello my name is {:10} Nice to meet you".format(name))
# print("Hello my name is {:<10} Nice to meet you".format(name))
# print("Hello my name is {:>10} Nice to meet you".format(name))
# print("Hello my name is {:^10} Nice to meet you".format(name))

# number = 1000
#
# print("The number pi is {:.3f}".format(number))
# print("The number is {:,}".format(number))
# print("The number is {:b}".format(number))
# print("The number is {:o}".format(number))
# print("The number is {:x}".format(number))
# print("The number is {:E}".format(number))

# random module

# import random
# x = random.randint(1, 6)
# y = random.random()
#
# myList = ['rock', 'paper', 'scissors']
# z = random.choice(myList)
#
# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "k", "A"]
#
# random.shuffle(cards)
# print(cards)
# print(z)
# print(x)
# print(y)

# exception handling = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers please.")
except Exception as e:
    print(e)
    print("Something went wrong.")
else:
    print(result)
finally:
    print("This will always execute.")


