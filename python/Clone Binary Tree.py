"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """

    def cloneTree(self, root):
        # Write your code here
        new_root = None
        if not root:
            return new_root
        new_root = TreeNode(root.val)

        def helper(root1, root2):
            if not root1:
                return
            if root1.left:
                root2.left = TreeNode(root1.left.val)
                helper(root1.left, root2.left)
            if root1.right:
                root2.right = TreeNode(root1.right.val)
                helper(root1.right, root2.right)
        helper(root, new_root)
        return new_root
