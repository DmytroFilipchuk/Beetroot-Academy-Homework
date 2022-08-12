"""
Task 1

A simple function.

Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
The function should then print “My favorite movie is named {name}”.

"""
def task1():
    def favourite_movie():
        user_fav_movie = input("Enter your favourite movie: ")
        print(f"Your favourite movie is named '{user_fav_movie}'")

    favourite_movie()

"""
Task 2

Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as parameters. 
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. 
Make the function print out the values of the dictionary to make sure that it works as intended.
"""
def task2():
    def make_country(**kwargs):
        for name, capital in kwargs.items():
            print(f"{name} - {capital}")

    make_country(Ukraine="Kyiv",Poland="Warsaw")


"""
Task 3

A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter 
(to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.
For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  
"""

def task3():
    def make_operation(operator,*args):
        numbers = args[0]
        for arg in args[1:]:
            if operator == "+":
                numbers += arg
            elif operator == "-":
                numbers -= arg
            elif operator == "*":
                numbers *= arg
        return numbers

    print(make_operation("-",2,4))

def task3_1():
    def make_operation(operator,*args):
        numbers = args[0]
        for arg in args[1:]:
            result = eval(str(numbers)+operator+str(arg))
            numbers = result
        return numbers

    print(make_operation("/",2,2))


def main():
    task1()
    task2()
    task3()
    task3_1()

if __name__ == '__main__':
    main()