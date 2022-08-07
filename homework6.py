"""
Task 1

The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers

"""
import random
def task1():
    print("TASK1")
    list_of_num = []

    while len(list_of_num) < 10:
        a = random.randint(1e9, 1e10)
        list_of_num.append(a)

    print(f"Random numbers with the length of 10: \n{list_of_num}\n")
    max_num = max(list_of_num)
    print(f"The largest number is: {max_num}\n")


"""
Task 2

Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, 
and make a third list containing the common integers between the 2 
initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers
"""
def task2():
    print("TASK2")
    list1 = []
    list2 = []

    def get_random(list):
        while len(list) < 10:
            num = random.randint(1, 10)
            list.append(num)

    get_random(list1)
    get_random(list2)
    print(f"Lists of random numbers from between 1 and 10: \n{list1}\n{list2}\n")
    list3 = []
    for num in list1:
        if num in list2 and num not in list3:
            list3.append(num)
    print(f"Common integers: \n{list3}\n")


"""
Task 3

Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list
that are divisible by 7 but not a multiple of 5, and store them in a separate list. 
Finally, print the list.

Constraint: use only while loop for iteration
"""

def task3():
    print("TASK3")
    # list_100 = [i for i in range(100) if i % 7 == 0 and i % 5 != 0]
    list_100 = [i for i in range(101)]
    divis_by_7 = []
    idx = 0
    while idx < len(list_100):
        number = list_100[idx]
        idx += 1
        if number % 7 == 0 and number % 5 != 0:
            divis_by_7.append(number)


    print(f"Numbers divisible by 7 but not a multiple of 5: \n{divis_by_7}")



def main():
    task1()
    task2()
    task3()

if __name__ == "__main__":
    main()