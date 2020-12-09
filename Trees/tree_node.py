# TreeNode Class
class TreeNode(object):
    # Constructor
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    # Method to get the data
    def get_data(self):
        return self.data
    
    # Method to set the data
    def set_data(self, data):
        self.data = data

    # Method to get the left link
    def get_left(self):
        return self.left

    # Method to set the left link
    def set_left(self, left):
        self.left = left
    
    # Method to get the right link
    def get_right(self):
        return self.right
    
    # Method to set the right link
    def set_right(self, right):
        self.right = right