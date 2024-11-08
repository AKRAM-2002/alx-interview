#!/usr/bin/python3
class Node:
    def __init__(self, data):
        self.data = data  # Assigns the given data to the node
        self.next = None  # Initialize the next attribute to null

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None
        
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the current head
        self.head = new_node  # Head now points to the new node

    def insertAtEnd(self, new_data): 
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line

    def reverse_linked_list(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next   # Step 1: Save the next node
            curr.next = prev        # Step 2: Reverse the link
            prev = curr             # Step 3: Move `prev` one step forward
            curr = next_node        # Step 4: Move `curr` one step forward
        return prev  # `prev` is the new head of the reversed list
    

if __name__ == '__main__':
    # Create a new LinkedList instance
    llist = LinkedList()

    # Insert each letter at the beginning using the method we created
    llist.insertAtBeginning('fox') 
    llist.insertAtBeginning('brown') 
    llist.insertAtBeginning('quick')  
    llist.insertAtBeginning('the')  

    llist.insertAtEnd('jumps')

    # Now 'the' is the head of the list, followed by 'quick', then 'brown' and 'fox'

    # Print the list

    print('Original Linked List:')
    llist.printList()
    
    # Reverse the linked list
    reversed_head = llist.reverse_linked_list()
    print(reversed_head)
    
    print('Reversed Linked List:')
    # Print the reversed list
    temp = reversed_head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next