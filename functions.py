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


def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


hello(last="Code", middle="Angel", first="Wendy")