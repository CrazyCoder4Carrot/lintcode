"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""

class Solution:	
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The count number in the interval [start, end] 
    def query(self, root, start, end):
        # write your code here
        if not root:
            return 0
        if start > end:
            return 0
        if start == root.start and end == root.end:
            return root.count
        if end > root.end:
            end = root.end
        mid = (root.start + root.end) / 2
        if root.start <= start and end <= mid:
            return self.query(root.left, start, end)
        if start > mid:
            return self.query(root.right, start, end)
        return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)