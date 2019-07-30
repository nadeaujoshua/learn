"""Module for implementing data structures"""

class NodeLinkedList:
    """A node class for LinkedList."""
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    """A linked list class using NodeLinkedList."""
    def __init__(self):
        self.head = None
    
    def add(self, value):
        """Create new node instance, append to end of current LinkedList."""
        new_node = NodeLinkedList(value)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
    
    def linear_search(self, value):
        """Search for given value within nodes linearly.
        
        Return index if value exists in list, or -1 if not.
        """
        current_node = self.head
        counter = 0
        while current_node:
            if current_node.value == value:
                return counter
            else:
                current_node = current_node.next
                counter += 1
        return -1


class MyStack:
    """A stack class using NodeLinkedList."""
    def __init__(self):
        self.top = None

    def peek(self):
        """Return the value of the most recent node."""
        top = self.top
        if top:
            return top.value

    def push(self, value):
        """Create new node, place at top of stack."""
        new_node = NodeLinkedList(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Remove and return most recent node."""
        to_pop = self.top
        if to_pop:
            self.top = to_pop.next
        return to_pop.value
            