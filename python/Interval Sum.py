"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class treeNode:
    def __init__(self, start, end, left = None, right = None):
        self.start = start
        self.end = end
        self.intervalsum = 0
        self.left = left
        self.right = right

class Solution:	
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    def intervalSum(self, A, queries):
        # write your code here
        if not A:
            return 0
        res = []
        low = 0
        high = len(A) - 1
        root = self.buildTree(A, low, high)
        for val in queries:
            res.append(self.query(root, val.start, val.end))
        return res
            
    def buildTree(self, A, low, high):
        if not A or low > high:
            return None
        mid = (low + high) / 2
        root = treeNode(low, high)
        if low == high:
            root.intervalsum = A[low]
            return root
        root.left = self.buildTree(A, low, mid)
        root.right = self.buildTree(A, mid + 1 , high)
        root.intervalsum = root.left.intervalsum + root.right.intervalsum
        return root
    def query(self, root, start, end):
        if not root or start > end:
            return 0
        if root.start == start and root.end == end:
            return root.intervalsum
        mid = (root.start + root.end) / 2
        if root.start <= start and end <= mid:
            return self.query(root.left, start, end)
        if mid < start:
            return self.query(root.right, start, end)
        return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)