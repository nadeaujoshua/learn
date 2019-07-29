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
