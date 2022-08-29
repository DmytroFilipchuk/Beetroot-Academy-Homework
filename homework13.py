"""
Task 1

Write a Python program to detect the number of local variables declared in a function.
"""
def task1():
    def fun():
        a = 3
        b = 7
        c = 4
        d = []
        return a,b,c,d

    def num_locals(func_name):
        return (func_name.__code__.co_nlocals)

    print(num_locals(fun))

"""
Task 2

Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""

def task2():
    # a * b + c

    def multiplication(a,b):
        c = a * b
        def add(d):
            #nonlocal c
            return c + d

        return add

    math_problem = multiplication(100,4)
    print(math_problem(4))

"""
Task 3

Write a function called `choose_func` which takes a list of nums and 2 callback functions. 
If all nums inside the list are positive, execute the first function on that list and return the result of it. 
Otherwise, return the result of the second one

 

def choose_func(nums: list, func1, func2):

    pass

 

# Assertions

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

 

def square_nums(nums):

    return [num ** 2 for num in nums]

 

def remove_negatives(nums):

    return [num for num in nums if num > 0]

 

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
"""

def task3():

    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]

    def square_nums(nums):
        return [num ** 2 for num in nums]

    def remove_negatives(nums):
        return [num for num in nums if num > 0]

    def choose_func(nums: list, func1, func2):

        def check(nums):
            return (all(x > 0 for x in nums))

        if check(nums):
            result = func1(nums)
        else:
            result = func2(nums)

        return result

    print(choose_func(nums1,square_nums,remove_negatives))



def main():
    task1()
    task2()
    task3()

if __name__ == '__main__':
    main()
