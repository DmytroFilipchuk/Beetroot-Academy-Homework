"""
Task 1

Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except state­ment to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
"""

def task1():
    def oops():
        raise IndexError

    def handle():
        try:
            oops()
        except IndexError:
            return "Index Error"

    print(handle())

"""
Task 2

Write a function that takes in two numbers from the user via input(), call the numbers a and b, 
and then returns the value of squared a divided by b, construct a try-except block which raises an 
exception if the two values given by the input function were not numbers, and if value b was zero
(cannot divide by zero).    
"""
def task2():
    def func():
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(a**2/b)
        except ValueError:
            print("Wrong input")
        except ZeroDivisionError:
            print("You can't divide by 0")

    func()



def main():
    task1()
    task2()

if __name__ == '__main__':
    main()
    
    
 TASKS WITH STAR

"""
Task1
Додати у функцію з 3-го завдання уроку 8 (A simple calculator),
обробку операції ділення. Врахувати можливий 0 у вхідних аргументах.
"""
from functools import reduce
from operator import mul,sub,truediv


def task1():
    def make_operation(operator,*args):
        if operator == "+":
            numbers = sum(args)
        if operator == "-":
            numbers = reduce(sub,args)
        if operator == "*":
            numbers = reduce(mul,args)
        if operator == "/":
            try:
                numbers = reduce(truediv, args)
            except ZeroDivisionError:
                print("You cannot divide by zero")
                exit()
        return numbers
    print(make_operation("/",2,4,6,0))

"""
Task2
Написати програму, яка на вхід приймає дату у форматі "1 January 22". 
Програма має вивести в консоль дати всіх понеділків в межах даного місяця.

"""
def task2():

    from datetime import datetime
    from dateutil import rrule
    import calendar

    while True:
        try:
            user_input = input("Enter a date in a following format '1 January 22': ")
            start_date = datetime.strptime(user_input, '%d %B %y').date()
        except ValueError:
            print("Wrong input")
            continue
        else:
            break


    last_day_of_mth= (calendar.monthrange(start_date.year,start_date.month)[1])
    end_date = datetime.strptime(f"{last_day_of_mth} {start_date.month} {start_date.year}", '%d %m %Y').date()
    all_mondays = []

    for date in rrule.rrule(rrule.DAILY, dtstart=start_date, until=end_date):
        if date.strftime("%A") == "Monday":
            all_mondays.append(date.strftime('%d %B %y'))

    print(f"\nThese are all mondays left in {start_date.strftime('%B %Y')}: \n{all_mondays}")


def main():
    task1()
    #task2()

if __name__ == '__main__':
    main()
