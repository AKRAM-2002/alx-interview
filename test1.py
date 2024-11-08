#!/usr/bin/python3
'''
Stack implementation using a list
'''
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
        
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  
        
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, val):
        '''Add an element to the end of the queue'''
        self.queue.append(val)
    
    def dequeue(self):
        '''Remove and return the element from the front of the queue. Return None if empty.'''
        if not self.is_empty():
            return self.queue.popleft()
        return None
    
    def peek(self):
        '''Return the front element without removing it. Return None if empty.'''
        if not self.is_empty():
            return self.queue[0]
        return None
    
    def is_empty(self):
        '''Check if the queue is empty'''
        return len(self.queue) == 0


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.peek()) 
    print(stack.pop())
    print(stack.pop())  # prints 20
    print(stack.pop())  # prints 10
    print(stack.pop())  # prints None
    print(stack.peek())  # prints None
    stack.push(40)
    print(stack.peek())  # prints 40


    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.peek())    # Output: 10
    print(queue.dequeue()) # Output: 10
    print(queue.dequeue()) # Output: 20
    print(queue.dequeue()) # Output: 30
    print(queue.dequeue()) # Output: None (empty queue)
    print(queue.peek())    # Output: None (empty queue)
    queue.enqueue(40)
    print(queue.peek())    # Output: 40