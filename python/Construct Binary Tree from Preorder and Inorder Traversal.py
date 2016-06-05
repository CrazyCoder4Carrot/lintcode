"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        rootindex = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:rootindex + 1], inorder[0: rootindex])
        root.right = self.buildTree(preorder[rootindex + 1:], inorder[rootindex + 1:])
        return root