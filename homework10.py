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