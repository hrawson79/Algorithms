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
        if (item == root.data):
            raise ValueError("Inserting duplicate item")

        # item is less than root
        if (item < root.data):
            root.left = self._subtree_insert(root.left, item)

        # item is greater than root
        if (item > root.data):
            root.right = self._subtree_insert(root.right, item)

        return root

    # Method to find an item in the tree
    def find(self, item):
        node = self.root

        while (node is not None and not(node.data == item)):
            if (item < node.data):
                node = node.left
            else:
                node = node.right
        
        if (node is None):
            return None
        else:
            return node.data

    # Method to remove item from the tree
    def delete(self, item):
        self.root = self._subtree_delete(root, item)

    # Helper method to remove item from the tree
    def _subtree_delete(self, root, item):
        # Empty tree, nothing to do
        if root is None:
            return None
        # Item is less than root
        if item < root.data:
            root.left = _subtree_delete(root.left, item)
        # Item is greater than root
        elif item > root.data:
            root.right = _subtree_delete(root.right, item)
        else:
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                root.item, root.left = self._subtree_del_max(root.left)
        return root
        
    # Helper method to promot the max
    def _subtree_del_max(self, root):
        if root.right is None:
            return root.item, root.left
        else:
            maxVal, root.right = self._subtree_del_max(root.right)
            return maxVal, root

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