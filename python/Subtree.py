"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def visit(self, root, string):
        if not root:
            string.append("#")
            return
        string.append(str(root.val))
        self.visit(root.left, string)
        self.visit(root.right, string)
        

    def isSubtree(self, T1, T2):
        # write your code here
        str1 = []
        self.visit(T1, str1)
        str2 = []
        self.visit(T2, str2)
        return ",".join(str2) in ",".join(str1)
        
        