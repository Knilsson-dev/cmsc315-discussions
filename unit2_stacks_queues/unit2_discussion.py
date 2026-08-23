"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.list = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        #Using .append() adds a new item to the end of the list, which is the top of the stack
        # Since pop() removes it from the end that makes the last thing to be entered the first thing to be removed
        self.list.append(value)
        print(f"Pushed: {self.list}")

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # We cant  remove or return an item that doesnt exist other wise this will result in a runtime error so to improve this i will implement a try statement to throw and exception
        # What should happen if the stack is empty?
        # If a stack is empty and pop is then used it should throw an exception

        try:
            self.list.pop()
            print(f"Popped: {self.list}")
        except IndexError as e:
            print(f"Error: {e}")



    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek returns the stacks top item but does not remove it and throws an exception if the stack is empty
        try:
            return self.list[-1]
        except IndexError as e:
            print(f"Error: {e}")


    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        if self.list == []:
            return True
        return False


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.queue = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        #Enqueue adds the value to the back of the list creating a clean line of values all in the order they were inputted ensuring that the first ones in will be at the front of the line.
        self.queue.append(value)
        print(f"Enqueued: {self.queue}")

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        #A queue cant be removed and returned when a value does not exist. So an if statement is required to throw and IndexError in the case of queue = null
        try:
            self.queue.popleft()
            print(f"Dequeued: {self.queue}")
        except IndexError as e:
            print(f"Error: {e}")


    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        #Front allows the user to return the value that is 1st in the queue aka the front of the line but does not remove it.
        try:
            self.queue[0]
            print(f"Front: {self.queue[0]}")
        except IndexError as e:
            print(f"Error: {e}")

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        if len(self.queue) == 0:
            return True
        else:
            return false


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.





print("\n=== STACK DEMO ===")
print("Demonstrate creating a stack object, add a min of 4 values and test the pop function to ensure lifo behavior")
#Create stack object
stackDemo = Stack()
#push 4 values into stack
stackDemo.push(1)
stackDemo.push(2)
stackDemo.push(3)
stackDemo.push(4)
#Pop the 4 values that were just pushed
stackDemo.pop()
stackDemo.pop()
stackDemo.pop()
stackDemo.pop()

print("Test for popping an empty stack which should raise IndexError and print a message")
stackDemo.pop()

print("Test for peeking an empty stack which should raise IndexError and print a message")
stackDemo.peek()

print("Verify that after we push a single value into ann empty stack and then pop that the stack does return as empty")
stackDemo.push(1)
stackDemo.pop()
print(f"Stack is empty: {stackDemo.is_empty()}")



# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("Create a queue object add a min of 4 values and test dequeue method to ensure fifo behavior ")
#Create the queue object
queueDemo = Queue()
#Enqueue 4 values
queueDemo.enqueue(1)
queueDemo.enqueue(2)
queueDemo.enqueue(3)
queueDemo.enqueue(4)
#Dequeue the values enqueued \
queueDemo.dequeue()
queueDemo.dequeue()
queueDemo.dequeue()
queueDemo.dequeue()

print("Test that the dequeue method throws IndexError and displays message on the empty queue")
queueDemo.dequeue()

print("Test that the front method throws IndexError and displays message on the empty queue")
queueDemo.front()
print("Add a single value to the empty queue followed by removing it to ensure the queue remains empty")
queueDemo.enqueue(1)
queueDemo.dequeue()
print(f"Queue is Empty: {queueDemo.is_empty()}")


if __name__ == "__main__":
    main()
