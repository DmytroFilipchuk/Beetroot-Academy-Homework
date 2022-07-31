"""
Task 1

The greeting program.

Make a program that has your name and the current day of the week
stored as separate variables and then prints a message like this:

 "Good day <name>! <day> is a perfect day to learn some python."
Note that  <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods
for constructing result string.
"""

name = "Dima"
day = "Sunday"
print(f"Good day {name}! {day} is a perfect day to learn some python.")
print("Good day %s! %s is a perfect day to learn some python." % (name,day))
print("Good day {}! {} is a perfect day to learn some python." .format (name,day))
print("Good day",name,"!",day,"is a perfect day to learn some python.")

"""
Task 2

Manipulate strings.

Save your first and last name as separate variables,
then use string concatenation to add them together 
with a white space in between and print a greeting.
"""

first_name = "Dmytro"
last_name = "Filipchuk"
full_name = first_name + " " + last_name
print("Good morning, " +  full_name + "!")

"""
Task 3

Using python as a calculator.

Make a program with 2 numbers saved in separate variables
a and b, then print the result for each of the following: 

Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division
"""

try:
    #global a, b
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    pass
except:
    print("Invalid input")
    exit()

addition = a + b
subtraction = a - b
division = a / b
multiplication = a * b
exponent = a ** b
modulus = a % b
floor_division = a // b

print(f"""
addition = {addition}
subtraction = {subtraction}
division = {division}
multiplication = {multiplication}
exponent = {exponent}
modulus = {modulus}
floor division = {floor_division}
""")

