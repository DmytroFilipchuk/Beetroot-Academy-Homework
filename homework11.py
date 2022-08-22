"""
Task1
Створити функцію, яка перетворює рядок в число без використання стандартних функцій. Спробуйте зробити без гугління.
"""
def task1():
    print("Не здогадався, як це виконати самостійно, розберу ідеї колег")



"""
Task2
Створити функцію, яка приймає на вхід список та число n. Вхідний список потрібно розбити на n максимально рівномірних
підсписків. Додатково можна зробити аргумент, який дозволить перевернути кожен із підсписків.
Приклад:
chunks([1, 2, 3, 4, 5, 6, 7], 3) -> [[1, 2], [3, 4], [5, 6, 7]]
"""
def task2():

    from math import floor
    numbers = [1,2,3,4,5,6,7,8,9,10,1,1,2,3,45,7,686,84,3]

    def func(my_list, n):

        elem_in_chunk = floor(len(my_list) / n)
        chunk = []
        new_list = []

        for el in my_list:
            chunk.append(el)
            if len(chunk) == elem_in_chunk:
                new_list.append(chunk)
                chunk = []

                if len(new_list) == n - 1:
                    the_rest = (n - 1) * elem_in_chunk
                    new_list.append(my_list[the_rest:])
                    break

        return new_list

    print(func(numbers, 8))

"""
Task 1

Files

Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
Then write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from 
the system command line. 
Does the new file show up in the directory where you ran your scripts? 

What if you add a different directory path to the filename passed to open?

Note: file write methods do not add newline characters to your strings; add an explicit ‘\n’ at the end of
the string if you want to fully terminate the line in the file.
"""

def task1_1():

    def file_write(filename="my_file.txt"):
        with open(filename, "w") as file:
            file.write("Hello file world!\n")

    def file_read(filename="my_file.txt"):
        with open(filename, "r") as file:
            return file.read()

    file_write()
    print(file_read())




def main():
    #task1()
    #task2()
    task1_1()

if __name__ == '__main__':
    main()

