#higher order function = a function that either accepts a function as an argument OR returns a function

# def loud(text):
#     return text.upper()
#
#
# def quiet(text):
#     return text.lower()
#
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
#
# hello(quiet)
# hello(loud)

#returns a function

def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))
