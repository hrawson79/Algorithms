# BinarySearchTree Class
from Trees.tree_node import TreeNode

class BinarySearchTree(object):
    # Constructor
    def __init__(self):
        self.root = None

    # Method to insert a new item into the tree
    def insert(self, item):
        self.root = self._subtree_insert(self.root, item)

    # Helper method to insert a new item recursively
    def _subtree_insert(self, root, item):
        # root is None
        if (root is None):
            return TreeNode(item)

        # item is equal to root
        if (item == root.get_data()):
            raise ValueError("Inserting duplicate item")

        # item is less than root
        if (item < root.get_data()):
            root.set_left(self._subtree_insert(root.get_left(), item))

        # item is greater than root
        if (item > root.get_data()):
            root.set_right(self._subtree_insert(root.get_right(), item))

        return root

    # Method to find an item in the tree
    def find(self, item):
        node = self.root

        while (node is not None and not(node.get_data() == item)):
            if (item < node.get_data()):
                node = node.get_left()
            else:
                node = node.get_right()
        
        if (node is None):
            return None
        else:
            return node.get_data()

    # Method to remove item from the tree
    def delete(self, item):
        self.root = self.root

    # Helper method to remove item from the tree
    def _subtree_delete(self, root, item):
        return None

    # Method to iterate the tree
    def __iter__(self):
        return self._inorder_gen(self.root)

    # Helper method to iterate inorder the tree
    def _inorder_gen(self, root):
        if root is not None:
            for item in self._inorder_gen(root.left):
                yield item
            yield root.get_data()
            for item in self._inorder_gen(root.right):
                yield item
    
    # Helper method to iterate preorder the tree
    def _preorder_gen(self, root):
        if root is not None:
            yield root.get_data()
            for item in self._preorder_gen(root.left):
                yield item
            for item in self._preorder_gen(root.right):
                yield item