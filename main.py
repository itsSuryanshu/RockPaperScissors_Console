import random
import os
#from colorama import init, Fore, Back, Style
# init()
os.system("clear")
a = (
    input("(!) Choose between ROCK, PAPER, SCISSORS [Type out the word]: ")).lower()
number = random.randint(0, 2)
choices = ["rock", "paper", "scissors"]
b = (choices[number])

print("(!) ROCK beats SCISSORS, PAPER beats ROCK, SCISSORS beats PAPER")
print(
    f"\n(=) You chose {a.upper()} and the computer chose {b.upper()}")
if a == b:
    print("\n(=) It's a TIE!")
elif a != b:
    if a == "rock" and b == "paper":
        print("(=) You LOST.")
    elif a == "rock" and b == "scissors":
        print("(=) You WIN!")
    elif a == "paper" and b == "rock":
        print("(=) You WIN!.")
    elif a == "paper" and b == "scissors":
        print("(=) You LOST.")
    elif a == "scissors" and b == "rock":
        print("(=) You LOST.")
    elif a == "scissors" and b == "paper":
        print("(=) You WIN!")
    else:
        print("(!!!) The game has stopped due to an ERROR")
