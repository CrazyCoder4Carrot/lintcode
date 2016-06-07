class treeNode:
    def __init__(self, start, end, left= None, right = None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        self.sumval = 0
class Solution:	
    
    # @param A: An integer list
    def __init__(self, A):
        if not A:
            return
        self.root = self.buildTree(A, 0 , len(A)-1)
        # write your code here
    def buildTree(self, A, low, high):
        if not A or low > high :
            return None
        root = treeNode(low, high)
        if low == high:
            root.sumval = A[low]
            return root
        mid = (low + high) / 2
        root.left = self.buildTree(A, low, mid)
        root.right = self.buildTree(A, mid + 1, high)
        root.sumval = root.left.sumval + root.right.sumval
        return root
    # @param start, end: Indices
    # @return: The sum from start to end
    def query(self, start, end):
        if start > end:
            return
        return self.queryRoot(self.root, start, end)
        # write your code here
    def queryRoot(self, root, start, end):
        if not root or start > end:
            return 0
        mid = (root.start + root.end) / 2
        if root.start == start and root.end == end:
            return root.sumval
        if root.start <= start and end < mid:
            return self.queryRoot(root.left, start, end)
        if mid < start:
            return self.queryRoot(root.right, start, end)
        return self.queryRoot(root.left, start, mid) + self.queryRoot(root.right, mid + 1, end)
        
    # @param index, value: modify A[index] to value.
    def modify(self, index, value):
        # write your code here
        self.modifyRoot(self.root, index, value)
    def modifyRoot(self, root, index, value):
        if not root:
            return
        if index < root.start or index > root.end:
            return 
        if root.start == index and root.end == index:
            root.sumval = value
            return
        mid = (root.start + root.end) / 2
        if index <= mid and index >= root.start:
            self.modifyRoot(root.left, index, value)
            
        if index > mid and index <= root.end:
            self.modifyRoot(root.right, index, value)
        root.sumval = root.left.sumval + root.right.sumval