# walrus operator (:=) = assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

