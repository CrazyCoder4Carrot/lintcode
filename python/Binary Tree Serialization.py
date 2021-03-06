"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        if not root:
            return []
        stack = [root]
        data = []
        while stack:
            levelstack = []
            for node in stack:
                if node:
                    data.append(node.val)
                    levelstack.append(node.left)
                    levelstack.append(node.right)
                else:
                    data.append('#')
            stack = levelstack
        i = len(data) - 1
        while i >= 0:
            if data[i] == '#':
                del data[i]
                i-=1
            else:
                return data
                

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        if not data:
            return None
        root = TreeNode(data[0])
        stack = [root]
        i = 1
        while stack:
            levelstack = []
            for node in stack:
                node.left = TreeNode(data[i]) if i < len(data) and data[i] != "#" else None
                i += 1
                if node.left:
                    levelstack.append(node.left)
                node.right = TreeNode(data[i]) if i < len(data) and data[i] != "#" else None
                i += 1
                if node.right:
                    levelstack.append(node.right)
            stack = levelstack
        return root