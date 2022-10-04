"""
Task 1

Write a program that reads in a sequence of characters
and prints them in reverse order, using your implementation of Stack.

"""

def task_1():

    stack = []
    word = "Beetroot"

    for char in word:
        stack.append(char)

    while stack:
        print(stack.pop())

"""
Task 2

Write a program that reads in a sequence of characters,
and determines whether it's parentheses, braces, and curly brackets are "balanced."

"""

def task_2():

    some_math = "[{}{}()]"
    open_signs = ["[", "(", "{"]
    close_signs = ["]", ")", "}"]
    #stack = []

    def balanced(data, open_signs, close_signs, stack=[]):

        for el in data:

            if el in open_signs:
                stack.append(el)

            elif el in close_signs:

                if close_signs.index(el) != open_signs.index(stack.pop()):
                    return "Unbalanced"

        if stack:
            return "Unbalanced"
        else:
            return "Balanced"

    print(balanced(some_math, open_signs, close_signs))


"""
Task 3

Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order. Consider the case in which the element is
not found - raise ValueError with proper info Message

Extend the Queue to include a method called get_from_stack that searches and returns
an element e from a queue. Any other element must remain in the queue respecting their
order. Consider the case in which the element is not found - raise ValueError with proper info Message
"""
def task_3():

    stack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    search_element = 2

    class Stack():

        def __init__(self, stack):
            self.stack = stack
            self.search_element = search_element
            self.temporary_stack = []

        def push(self, data):
            self.stack.append(data)

        def pop(self):
            if self.stack:
                return self.stack.pop()
            else:
                return None

        def size(self):
            return len(self.stack)

        def empty(self):
            return True if self.size() == 0 else False

        def peek(self):
            return self.stack[-1]

        def get_from_stack(self, search_element):

            if self.empty():
                return "Stack is empty"

            found_status = False

            while self.stack:

                current_element = self.stack.pop()

                if current_element != search_element:
                    self.temporary_stack.append(current_element)
                else:
                    found_status = True
                    break

            if not found_status:
                raise ValueError("Not Found")

            while self.temporary_stack:
                self.stack.append(self.temporary_stack.pop())

            return f"Here you go : {current_element}\n{self.stack = }"

    a = Stack(stack)
    print(a.get_from_stack(search_element))

    from queue import Queue

    class MyQueue(Queue):

        def __init__(self, queue):
            super(MyQueue, self).__init__()
            self.queue = queue
            self.temporary_queue = []

        def get_from_queue(self,search_element):

            if self.empty():
                return "Stack is empty"

            found_status = False

            while self.queue:

                current_element = self.queue.pop()

                if current_element != search_element:
                    self.temporary_queue.append(current_element)
                else:
                    found_status = True
                    break

            if not found_status:
                raise ValueError("Not Found")

            while self.temporary_queue:
                self.queue.append(self.temporary_queue.pop())

            return f"Here you go : {current_element}\n{self.queue = }"

    b = MyQueue(stack)
    b.put(11)
    print(b.get_from_queue(11))

def main():
    #task_1()

    try:
        task_2()
    except IndexError:
        print("Unbalanced")

    #task_3()


if __name__ == '__main__':
    main()


