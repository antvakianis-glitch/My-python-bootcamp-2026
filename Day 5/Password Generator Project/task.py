import random
import sys
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
try:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    if (nr_letters or nr_symbols or nr_numbers) <= 0:
        print("Invalid input")
except ValueError:
        print("Enter only numbers")
        sys.exit()
number1 = []
for let in range(nr_letters):
    number1.append(random.choice(letters))
for symbol in range(nr_symbols):
    number1.append(random.choice(symbols))
for number in range(nr_numbers):
    number1.append(random.choice(numbers))
random.shuffle(number1)
print("Here is your password:")
print(*number1, sep="")
