# lambda = func written in 1 line using lambda keyword
#          accepts any number of arguments, but only one expression
#          useful if needed for a short period of time

# def double(x):
#     return x * 2
# print(double(5))


double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
# print(double(5))
# print(multiply(5, 6))
print(add(5, 6, 7))

