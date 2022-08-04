"""
Task 1

The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
"""
from random import randrange

random_num = randrange(10)
try:
    user_input = int(input("Guess a number between 1 and 10: "))
except:
    print("Wrong input")
    exit()

if user_input == str(random_num):
    print("Yeeeeah")
else:
    print(f"Sorry. The correct number is {random_num}")

"""
Task 2

The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”   
 
"""
try:
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
except:
    print("Wrong input")
    exit()

print(f"Hello {user_name}, on your next birthday you'll be {user_age + 1} years")

"""
Task 3

Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.

For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 

'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
Tips: Use random module to get random char from string)
"""
import random

user_input = input("Text sth: ")
length = len(user_input)
num = 5
start = 0

while start < num:
    result = ''.join((random.choice(user_input)) for x in range(length))
    print(f"{result}\n")
    start += 1
