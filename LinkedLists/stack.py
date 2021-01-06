# Stack Class
from LinkedLists.list_node import ListNode

class Stack(object):
    # Constructor
    def __init__(self):
        self.top = None
        self.size = 0

    # Method to return the size of the stack
    def __len__(self):
        return self.size

    # Method to add an item to the stack
    def push(self, item):
        if (self.size == 0):
            self.top = ListNode(item)
        else:
            node = self.top
            self.top = ListNode(item, node)
        self.size += 1

    # Method to remove an item from the stack
    def pop(self):
        node = None
        if (self.size > 0):
            node = self.top
            self.top = self.top.get_link()
            self.size -= 1
        return node
    
    # Method to retrieve the top item from the stack without removing
    def get_top(self):
        return self.top

    # Method to retrive the size of the stack
    def get_size(self):
        return self.size

    # Method to iterate the stack
    def __iter__(self):
        current_node = self.top
        while current_node is not None:
            yield current_node.get_item()
            current_node = current_node.get_link()