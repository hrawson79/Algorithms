# List Node Class
class ListNode(object):
    # Constructor
    def __init__(self, item = None, link = None):
        self.item = item
        self.link = link

    # Get method to return the data element of the node
    def get_item(self):
        return self.item

    # Set method to set the data element of the node
    def set_item(self, item):
        self.item = item

    # Get method to return the link stored at the node
    def get_link(self):
        return self.link

    # Set method to set the link stored at the node
    def set_link(self, link):
        self.link = link