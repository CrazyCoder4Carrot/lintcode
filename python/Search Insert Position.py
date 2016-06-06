class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        i = 0
        while i < len(A):
            if A[i] >= target:
                break
            i += 1
        return i
            