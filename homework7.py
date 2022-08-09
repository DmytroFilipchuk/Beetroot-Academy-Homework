"""
Task 1

Make a program that has some sentence
(a string) on input and returns a dict containing all unique words
as keys and the number of occurrences as values.
"""

def task1():
    print("TASK1\n")
    def word_count(sentence):
        counts = dict()
        words = sentence.split()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        return counts

    sentence = input("Type some words: ").lower()
    print(word_count(sentence))

"""
Task 2

Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

Compute the total price of the stock where the total price is the sum 
of the price of an item multiplied by the quantity of this exact item.
"""

def task2():
    print("\nTASK2\n")
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    total_for_each = {item: prices[item]*stock[item] for item in stock}
    total = sum(prices[item]*stock[item] for item in stock)
    print(f"Total for each item: \n{total_for_each}\n")
    print(f"Global total is: {total}\n")

"""
Task 3

List comprehension exercise

Use a list comprehension to make a list containing tuples (i, j)
where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
"""
def task3():
    print("\nTASK3\n")
    #list = [tuple([i for i in range(1, 11)],),tuple([i**2 for i in range(1,11)])]
    list1 = [i for i in range(1, 11)]
    list2 = [i ** 2 for i in range(1, 11)]
    list3 = [i for i in zip(list1, list2)]
    print(list3)


"""
Task 4

Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,
"""

def task4():
    print("\nTASK4\n")
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dict = {idx+1:day for (idx,day) in enumerate(days) }
    dict_reversed = {value: key for key, value in dict.items()}
    print(dict)
    print(dict_reversed)


























def main():
    task1()
    task2()
    task3()
    task4()


if __name__ == '__main__':
    main()