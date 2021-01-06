# Queue Class
from LinkedLists.list_node import ListNode

class Queue(object):
    # Constructor
    def __init__(self):
        self.front = None
        self.end = None
        self.size = 0

    # Method to return the size of the queue
    def __len__(self):
        return self.size

    # Method to add item to the queue
    def enqueue(self, item):
        if (self.size == 0):
            self.front = ListNode(item)
            self.end = self.front
        else:
            node = ListNode(item)
            self.end.set_link(node)
            self.end = node

        self.size += 1

    # Method to remove next item from the queue
    def dequeue(self):
        node = None
        if (self.size > 0):
            node = self.front
            self.front = node.get_link()
            self.size -= 1
        return node

    # Method to retrieve the front item without removing it
    def get_front(self):
        return self.front

    # Method to retrieve the size of the queue
    def get_size(self):
        return self.size

    # Method to iterate the queue
    def __iter__(self):
        current_node = self.front
        while current_node is not None:
            yield current_node.get_item()
            current_node = current_node.get_link()