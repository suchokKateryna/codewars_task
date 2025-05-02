# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    '''class solution'''
    def delete_node(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root

        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Node has two children, find the in-order successor (smallest in the right subtree)
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val
                root.right = self.delete_node(root.right, successor.val)
        return root
