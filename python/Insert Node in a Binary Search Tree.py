"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
"""
Revursive version
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if not root:
            root = node
            return root
        if root.val > node.val:
            if not root.left:
                root.left = node
            else:
                self.insertNode(root.left, node)
            return root
        else:
            if not root.right:
                root.right = node
            else:
                self.insertNode(root.right, node)
            return root
"""
Iteration version
"""

class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if not root:
            root = node
            return root
        cur = root
        while cur:
            if cur.val > node.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = node
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = node
                    break
        return root

"""
Refined iteration version
"""
