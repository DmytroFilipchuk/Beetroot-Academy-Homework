"""
Task 1

Extend UnorderedList

Implement append, index, pop, insert methods for UnorderedList.
Also implement a slice method, which will take two parameters `start` and `stop`,
and return a copy of the list starting at the position and going up to but not including the stop position.

"""

def task_1():
    class Node:
        def __init__(self, data):
            self._data = data
            self._next = None

        def get_data(self):
            return self._data

        def get_next(self):
            return self._next

        def set_data(self, data):
            self._data = data

        def set_next(self, new_next):
            self._next = new_next

    class UnorderedList:

        def __init__(self):
            self._head = None

        def is_empty(self):
            return self._head is None

        def add(self, item):
            temp = Node(item)
            temp.set_next(self._head)
            self._head = temp

        def append(self, item):

            temp = Node(item)
            current = self._head
            count = 0

            while count < self.size() - 1:
                count += 1
                current = current.get_next()

            current.set_next(temp)
            temp.set_next(None)

        def get_index(self, item):

            current = self._head
            found = False
            count = 0

            while current is not None and not found:

                if current.get_data() == item:
                    found = True
                    break
                else:
                    current = current.get_next()

                count += 1

            if found is False:
                raise ValueError(f"There is no {item} element")

            return count

        def pop(self):

            current = self._head
            count = 0

            while count < self.size() - 2:
                count += 1
                current = current.get_next()

            popped_data = current.get_next().get_data()

            current.set_next(None)

            return popped_data

        def slice(self, start, stop):

            current = self._head
            found = False
            slicing = []

            while current is not None and not found:
                if current.get_data() == start:
                    found = True
                    self._head = current
                else:
                    current = current.get_next()

            if found is False:
                raise ValueError(f"There is no {start} element")

            found = False

            while current is not None and not found:
                if current.get_data() == stop:
                    found = True
                else:
                    slicing.append(current.get_data())
                    current = current.get_next()

            if found is False:
                raise ValueError(f"There is no {stop} element")

            return slicing

        def size(self):
            current = self._head
            count = 0
            while current is not None:
                count += 1
                current = current.get_next()

            return count

        def search(self, item):
            current = self._head
            found = False
            while current is not None and not found:
                if current.get_data() == item:
                    found = True
                else:
                    current = current.get_next()

            return found

        def remove(self, item):
            current = self._head
            previous = None
            found = False
            while not found:
                if current.get_data() == item:
                    found = True
                else:
                    previous, current = current, current.get_next()

            if previous is None:
                self._head = current.get_next()
            else:
                previous.set_next(current.get_next())

        def __repr__(self):
            representation = "<UnorderedList: "
            current = self._head
            while current is not None:
                representation += f"{current.get_data()} "
                current = current.get_next()
            return representation + ">"

        def __str__(self):
            return self.__repr__()

    if __name__ == "__main__":
        my_list = UnorderedList()

        my_list.add(31)
        my_list.add(77)
        my_list.add(17)
        my_list.add(32)
        my_list.add(55)
        my_list.add(95)
        my_list.add(13)
        my_list.add(0)

        print(my_list)
        print(my_list.slice(95,31))
        print(my_list.pop())
        print(my_list)

"""
Task 2

Implement a stack using a singly linked list

"""

def task_2():

    class Node:

        def __init__(self, data):
            self._data = data
            self._next = None

        def get_data(self):
            return self._data

        def get_next(self):
            return self._next

        def set_data(self, data):
            self._data = data

        def set_next(self, new_next):
            self._next = new_next

    class Stack:

        def __init__(self):
            self._head = None

        def is_empty(self):
            return self._head is None

        def push(self, data):

            if self.is_empty():
                self._head = Node(data)

            else:
                new_node = Node(data)
                new_node._next = self._head
                self._head = new_node

        def pop(self):

            if self.is_empty():
                return None

            popped_node = self._head
            self._head = self._head._next
            popped_node.next = None

            return popped_node._data

        def peek(self):

            if self.is_empty():
                return None

            else:
                return self._head._data

        def display(self):

            current = self._head

            if self.is_empty():
                print("Stack is empty")

            else:

                while current is not None:
                    print(current._data, "->", end=" ")
                    current = current._next
                return

        def __repr__(self):

            representation = "<SinglyLinkedList: "
            current = self._head
            while current is not None:
                representation += f"{current.get_data()} "
                current = current.get_next()
            return representation + ">"

        def __str__(self):
            return self.__repr__()


    MyStack = Stack()
    MyStack.push(11)
    MyStack.push(22)
    MyStack.push(33)
    MyStack.push(44)
    print(MyStack)
    print(MyStack.pop())
    print(MyStack.peek())
    print(MyStack)

if __name__ == '__main__':
    #task_1()
    task_2()