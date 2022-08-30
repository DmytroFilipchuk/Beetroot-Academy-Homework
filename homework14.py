"""
Task 1

Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!

For example:

 "add called with 4, 5"

```

def logger(func):

    pass



@logger

def add(x, y):

    return x + y



@logger

def square_all(*args):

    return [arg ** 2 for arg in args]

```

"""

"""def first(func):
    def wrap():
        print("s")
        func()
        print("r")
    return wrap
"""



from functools import wraps

def task1():
    def logger(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            print(f"{func.__name__} called with:{[arg for arg in args]}")
            func(*args, **kwargs)

        return wrap

    @logger
    def add(x, y):
        return x + y

    @logger
    def square_all(*args):
        return [arg ** 2 for arg in args]

    add(5, 5)
    square_all(2, 4, 6)


"""
Task 2

Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

```

def stop_words(words: list):

    pass

 

@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"

 

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

```
"""

def task2():

    list_of_stop_words = ['pepsi', 'BMW']

    def stop_words(list_of_stop_words):

        def inner(func):

            @wraps(func)
            def wrap(*args, **kwargs):
                sentence = func(*args, **kwargs)

                for i in list_of_stop_words:

                    if i in sentence:
                        new_sentence = sentence.replace(i, "*")
                        sentence = new_sentence

                return new_sentence
            return wrap
        return inner





    @stop_words(list_of_stop_words)
    def create_slogan(name = "Jake"):
        return f"{name} drinks pepsi in his brand new BMW!"

    print(create_slogan("Mike"))



def main():
    task1()
    task2()


if __name__ == '__main__':
    main()