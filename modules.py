# import messages as msg
#
# msg.hello()
# msg.bye()

# from messages import hello, bye
# hello()
# bye()

# help("modules")


#rock, paper, scissors games
import random
choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

player = input("rock, paper, or scissors?: ")

print(computer)