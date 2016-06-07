class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        length = len(A)
        if not A:
            return []
        l = [1] * length
        r = [1] * length
        for i in range(1, len(A)):
            l[i] = l[i-1] * A[i-1]
        for i in range(0, len(A) - 1)[::-1]:
            r[i] = r[i + 1] * A[i + 1]
        res = [0] * len(A)
        for i in range(len(A)):
            res[i] = l[i] * r[i]
        return res