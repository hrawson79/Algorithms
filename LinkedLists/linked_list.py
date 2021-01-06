# LList Class
from LinkedLists.list_node import ListNode

class LList(object):
    # Constructor
    def __init__(self, seq=()):
        # Initialize
        self.head = None
        self.tail = None
        self.size = 0

        # If passed seq, append each to linked list
        for item in seq:
            self.append(item)

    # Method to return the length of the linked list
    def __len__(self):
        return self.size

    # Method to find the node at position
    def _find(self, position):
        assert 0 <= position < self.size

        node = self.head
        for i in range(position):
            node = node.link
        return node

    # Method to append item at end of list
    def append(self, item):
        newNode = ListNode(item)

        if self.head is not None:
            self.tail.set_link(newNode)
        else:
            self.head = newNode
        self.tail = newNode
        self.size += 1
    
    # Method to get item at position
    def __getitem__(self, position):
        node = self._find(position)
        
        return node.item

    # Method to set item at position
    def __setitem__(self, position, item):
        node = self._find(position)

        node.set_item(item)

    # Helper method to delete item from list
    def _delete(self, position):
        if position == 0:
            # Save item to return
            item = self.head
            # Delete by setting head to link of head
            self.head = self.head.get_link()
            if self.size == 1:
                self.tail = None
        else:
            # Find the node before the one to be deleted
            prevNode = self._find(position-1)
            # Save item to return
            item = prevNode.get_link().get_item()
            # Delete by setting previous link to link of deleted node
            prevNode.set_link(prevNode.get_link().get_link())
            if position == self.size - 1:
                self.tail = prevNode
        self.size -= 1
        return item

    # Method to delete item from list at position
    def __delitem__(self, position):
        assert 0 <= position < self.size

        self._delete(position)

    # Method to pop item from list at position
    def pop(self, position = None):
        assert self.size > 0 and (position is None or (0 <= position < self.size))

        # If position not specified, set to the last node as a default
        if (position is None):
            position = self.size - 1
        
        return self._delete(position)

    # Method to insert item into list at position
    def insert(self, item, position):
        assert 0 <= position <= self.size

        # If list size is 0 or inserting at end of list, simple append
        if self.size == 0 or position == self.size:
            self.append(item)
        # Else if position is beginning of list
        elif position == 0:
            node = self.head
            self.head = ListNode(item, node)
        # Else find position to insert
        else:
            prevNode = self._find(position - 1)
            prevNode.set_link(ListNode(item, prevNode.get_link()))
        self.size += 1

    # Method to make a copy of a list
    def __copy__(self):
        a = LList()
        for i in range(self.size):
            a.append(self[i])
        return a

    # Method to iterate the list
    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.get_item()
            current_node = current_node.get_link()