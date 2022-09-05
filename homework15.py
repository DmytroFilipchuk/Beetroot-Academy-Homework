"""Task 1

A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them
as attributes. Make another method called talk() which makes prints a greeting from the person containing,
for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

"""

def task_1():
    class Person:

        def __init__(self,firstname,lastname,age):
            self.firstname = firstname
            self.lastname = lastname
            self.age = age

        def talk(self):
            return f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old"



    person = Person("Carl", "Johnson", 26)
    print(person.talk())


"""
Task 2

Doggy age

Create a class Dog with class attribute `age_factor` equals to 7. 
Make __init__() which takes values for a dog’s age. Then create a method `human_age`
which returns the dog’s age in human equivalent.
"""


def task_2():
    class Dog:
        age_factor = 7

        def __init__(self, dog_age):
            self.dog_age = dog_age

        def human_age(self):
            return self.dog_age * self.age_factor

    dog_1 = Dog(10)
    print(dog_1.human_age())


"""
Task 3

TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
exists in the list, or "No" - in the other case.
 

The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.

```

CHANNELS = ["BBC", "Discovery", "TV1000"]

 class TVController:

pass

 controller = TVController(CHANNELS)

controller.first_channel() == "BBC"

controller.last_channel() == "TV1000"

controller.turn_channel(1) == "BBC"

controller.next_channel() == "Discovery"

controller.previous_channel() == "BBC"

controller.current_channel() == "BBC"

controller.is_exist(4) == "No"

controller.is_exist("BBC") == "Yes"

"""


def task_3():

    from functools import wraps

    class TVController:
        CHANNELS = ["BBC", "Discovery", "TV1000","TNT","1+1"]
        Current_channel = ""
        Number = 0

        def __init__(self):
            pass

        def first_channel(self):
            return self.CHANNELS[0]

        def last_channel(self):
            return self.CHANNELS[-1]

        def no_channel(func):
            @wraps(func)
            def wrap(self,*args):
                try:
                    return func(self, *args)
                except IndexError:
                    return f"There is no channel number {args[0]}"
            return wrap

        @no_channel
        def turn_channel(self, number):
            self.Current_channel = self.CHANNELS[number - 1]
            self.Number = number
            return self.Current_channel

        def next_channel(self):
            if self.Current_channel == self.CHANNELS[-1]:
                self.Current_channel = self.CHANNELS[0]
                return self.Current_channel
            else:
                self.Current_channel = self.CHANNELS[self.Number]
                return self.Current_channel

        def previous_channel(self):
            if self.Current_channel == self.CHANNELS[0]:
                self.Current_channel = self.CHANNELS[-1]
                return self.Current_channel
            else:
                self.Current_channel = self.CHANNELS[self.Number - 1]
                return self.Current_channel

        def current_channel(self):
            return self.Current_channel

        def is_exist(self, find_me):

            if str(find_me).isdigit():
                if find_me > len(self.CHANNELS):
                    return "No"
                else:
                    return "Yes"
            else:
                if find_me not in self.CHANNELS:
                    return "No"
                else:
                    return "Yes"

    controller = TVController()

    print(controller.first_channel())

    print(controller.last_channel())

    print(controller.turn_channel(6))

    print(controller.next_channel())

    print(controller.previous_channel())

    print(controller.current_channel())

    print(controller.is_exist("TNT"))






























def main():
    #task_1()
    #task_2()
    task_3()


if __name__ == '__main__':
    main()