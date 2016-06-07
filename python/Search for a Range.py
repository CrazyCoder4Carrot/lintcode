class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
        
        low = 0
        high = len(A) - 1
        while low != high:
            if A[low] == target and A[high] == target:
                break
            if A[low] < target:
                low += 1
            if A[high] > target:
                high -= 1
        if low == high and A[low] != target:
            return [-1,-1]
        else:
            return [low, high]