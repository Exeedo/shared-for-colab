"""
-- Linked List -- Part 1+2 --

This is a part of the DDDS Guide. Prepared by Osama Khallouf.

Original file is located at:
    https://colab.research.google.com/drive/1GG6x3Pnqfbu_PNi9s4Y4tWPtyz4RETDo
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.size == 0:
            # For an empty list, the new node becomes the head
            self.head = new_node
        else:
            # Otherwise, we will go to the end of the list
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            # NOTE: Alternatively, you can use a for-loop with the value of `self.size - 1`
            # Now we add the new node after the last node `current_node`
            # Don't worry, this is using a pointer to `new_node`, not a separate copy
            current_node.next = new_node
        # Do not forget to increment the size
        self.size += 1

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            # For an empty list, the new node becomes the head
            self.head = new_node
        else:
            # Otherwise, the new node still becomes the head, but the original
            # head becomes its next node
            new_node.next = self.head
            self.head = new_node
        # Do not forget to increment the size
        self.size += 1

    def insert_at(self, data, index):
        if index < 0 or index > self.size:
            # This case is not allowed. You can either return from the function
            # without updating the list, or raise an error to inform the user
            # of a non-allowed operation
            raise IndexError(f"Index {index} is out of range.")

        if index == 0:
            # We already have this function
            self.insert_at_beginning(data)
        elif index == self.size:
            # We already implemented this
            self.insert_at_end(data)
        else:
            # We need to get the node just before the provided index
            current = self.head
            for _ in range(index - 1):
                current = current.next

            # Now we need to link the next of the new node to the existing next
            # of `current` and link the next of `current` to the new node
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

            # Do not forget to increment the size
            self.size += 1

