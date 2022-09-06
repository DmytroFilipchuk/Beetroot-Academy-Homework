"""
Task 1

School

Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute,
while salary should only be available to the teacher.

"""
def task_1():
    class Person():
        def __init__(self, firstname, secondname):
            self.firstname = firstname
            self.secondname =secondname


    class Student(Person):
        def __init__(self,firstname, secondname, year, exam_status):
            super().__init__(firstname, secondname)
            self.year = year
            self.exam_status = exam_status

        def next_year_of_study(self):
            if self.exam_status == "Passed":
                self.year += 1
            else:
                print(f"{self.firstname} {self.secondname} can't be moved to the next year")


    class Teacher(Person):
        def __init__(self,firstname, secondname, salary):
            super().__init__(firstname, secondname)
            self.salary = salary

        def salary_rise(self,rise_amount):
            self.salary += rise_amount


    student1 = Student("Dima","Philipchuk",2,"In progress")
    student2 = Student("Max","Vyshnevski",1,"Passed")
    student1.next_year_of_study()
    student2.next_year_of_study()
    print(student1.year)
    print(student2.year)
    teacher1 = Teacher("Vasyl","Petrenko",10000)
    print(teacher1.salary)
    teacher1.salary_rise(200)
    print(teacher1.salary)


"""
Task 2

Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
```

class Mathematician:

    pass

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
"""
def task_2():
    class Mathematician():

        def square_nums(self,numbers):
            return [i * i for i in numbers]

        def remove_positives(self,numbers):
            return [i for i in numbers if i < 0]

        def filter_leaps(self,numbers):
            return [i for i in numbers
                if ((i % 400 == 0) or
                    (i % 100 != 0) and
                    (i % 4 == 0))]

    m = Mathematician()

    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

