"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    # @oaram A: a list of integer
    # @return: The root of Segment Tree
    def build(self, A):
        # write your code here
        if not A:
            return 
        return self.buildTree(A, 0, len(A) - 1)
        
    def buildTree(self, A, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        root = SegmentTreeNode(start, end)
        if start == end:
            root.max = A[start]
            return root
        root.left = self.buildTree(A, start, mid)
        root.right = self.buildTree(A, mid + 1, end)
        root.max = max(root.left.max, root.right.max)
        return root