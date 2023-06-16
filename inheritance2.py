#multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:

    alive = True

class Animal(Organism):
    def eat(self):
        print("this animal is eating.")

class Dog(Animal):
    def bark(self):
        print("This dog is barking.")