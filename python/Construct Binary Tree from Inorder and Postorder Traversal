"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        rootindex = inorder.index(root.val)
        root.left = self.buildTree(inorder[:rootindex], postorder[:rootindex])
        root.right = self.buildTree(inorder[rootindex + 1:],postorder[rootindex:-1])
        return root