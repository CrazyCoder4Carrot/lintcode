"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:	
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]
    def query(self, root, start, end):
        # write your code here
        if start > end:
            return 
        if not root:
            return
        if start == root.start and end == root.end:
            return root.max
        mid = (root.start + root.end)/2
        if root.start <= start and end <= mid:
            return self.query(root.left, start, end)
        if start > mid:
            return self.query(root.right, start, end)
        return max(self.query(root.left, start, mid), self.query(root.right, mid + 1, end))
        