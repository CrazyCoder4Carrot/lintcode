"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: A list of list of integer include 
             the zig zag level order traversal of its nodes' values
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if not root:
            return []
        stack = [root]
        flag  = True
        res = []
        while stack:
            levelstack = []
            levelres = []
            for node in stack:
                levelres.append(node.val)
                if node.left:
                    levelstack.append(node.left)
                if node.right:
                    levelstack.append(node.right)
            if flag:
                res.append(levelres)
            else:
                res.append(levelres[::-1])
            flag = not flag
            stack = levelstack
        return res