"""
Task 1

String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string.

Sample String: 'helloworld'

Expected Result : 'held'

Sample String: 'my'

Expected Result : 'mymy'

Sample String: 'x'

Expected Result: Empty String

Tips:

Use built-in function len() on an input string
Use positive indexing to get the first characters of a string and negative indexing to get the last characters
"""
import random
import sys
number = 2
def main():
    string = sys.argv[1]
    if len(string)<number:
       print(" ")
    else:
       print(string[0:2]+string[-2:])


"""
Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical characters and is only 10 characters long. 
Print a suitable message depending on the outcome of the string evaluation.
"""

num_of_characters = 10
phone_number = str(input("Enter your phone number: "))
is_digit = phone_number.isdigit()

if not is_digit:
    print("Please use only numerical characters")
elif len(phone_number) != num_of_characters:
    print("Wrong number of characters")
elif phone_number[0] == "7":
    print("The phone number cannot start with 7")
else:
    print("Thank you!")

if phone_number[0:3] == "050" :
    print("Мтс")
elif phone_number[0:3] == "067" or "068" :
    print("Київстар")
elif phone_number[0:3] == "099" :
    print("Vodafone")

"""
Task 3

The math quiz program.

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, 
and then responds with a message accordingly.
"""
from random import randrange

num_1 = randrange(100)
num_2 = randrange(100)
str_num_1 = str(num_1)
str_num_2 = str(num_2)

expressions = [
str_num_1 + "+" + str_num_2,
str_num_1 + "-" + str_num_2,
str_num_1 + "/" + str_num_2,
str_num_1 + "*" + str_num_2,
]

random_expression = random.choice(expressions)

if "+" in random_expression:
    result = num_1 + num_2
elif "-" in random_expression:
    result = num_1 - num_2
elif "/" in random_expression:
    result = num_1 / num_2
else:
    result = num_1 * num_2

try:
    user_input = float(input(random_expression + " =  "))
except:
    print("Use only numerical characters")
    #exit()

if user_input == result :
    print("Good job!")
else:
    print(f"Try again! Correct answer is {result}")

"""
Task 4

The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
The program should check if your input is equal to the stored name even if the given name has another case, e.g., 
if your input is “Anton” and the stored name is “anton”, it should return True.
"""

list_of_names = ["dima","anton","sasha"]
try:
    user_input1 = str(input("Enter your name:  "))
except:
    print("Try again")
    exit()
user_input1_lower = user_input1.lower()

if user_input1_lower in list_of_names:
    print("True")
else:
    print("False")










