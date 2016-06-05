"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        # write your code here
        temp = []
        if not root:
            return []
        if k1 > k2:
            return []
        res= []
        self.visit(root, temp)
        for val in temp:
            if val >= k1 and val <= k2:
                res.append(val)
        return res
    def visit(self, root, temp):
        if not root:
            return 
        if root.left:
            self.visit(root.left, temp)
        temp.append(root.val)
        if root.right:
            self.visit(root.right, temp)
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
"""
Recursive 274ms
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        # write your code here
        temp = []
        if not root:
            return []
        if k1 > k2:
            return []
        res= []
        self.visit(root, res, k1, k2)
        return res
    def visit(self, root, temp, k1, k2):
        if not root:
            return 
        if root.val < k1 :
            self.visit(root.right, temp, k1, k2)
        if root.val > k2:
            self.visit(root.left, temp, k1, k2)
        if root.val >= k1 and root.val <= k2:
            self.visit(root.left, temp, k1, k2)
            if root.val >= k1 and root.val <= k2:
                temp.append(root.val)
            self.visit(root.right, temp, k1, k2)