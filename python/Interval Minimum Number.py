"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class treeNode:
    def __init__(self, low, high, left= None, right = None):
        self.low = low
        self.high = high
        self.left= left
        self.right = right
        self.minval = 0
import sys
class Solution:	
    """
    @param A, queries: Given an integer array and an Interval list
                       The ith query is [queries[i-1].start, queries[i-1].end]
    @return: The result list
    """
    def buildTree(self, A, low, high):
        if not A or low > high:
            return None
        root = treeNode(low, high)
        mid = (low + high) / 2
        if low == high:
            root.minval = A[low]
            return root
        root.left = self.buildTree(A, low, mid)
        root.right = self.buildTree(A, mid + 1, high)
        root.minval = min(root.left.minval, root.right.minval)
        return root
    def visit(self, root):
        if not root:
            return
        print root.low, root.high, root.minval
        self.visit(root.left)
        self.visit(root.right)
    def query(self, root, low, high):
        if not root:
            return 0
        
        if root.low == low and root.high == high:
            return root.minval
        mid = (root.low + root.high) / 2
        if low >= root.low and high <= mid :
            return self.query(root.left, low, high)
        if low > mid:
            return self.query(root.right, low, high)
        return min(self.query(root.left, low, mid), self.query(root.right, mid + 1, high))
    def intervalMinNumber(self, A, queries):
        # write your code here
        root = self.buildTree(A, 0, len(A) - 1)
        #self.visit(root)
        res = []
        for val in queries:
            res.append(self.query(root, val.start, val.end))
        return res