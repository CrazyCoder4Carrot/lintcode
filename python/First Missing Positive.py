class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        if not A:
            return 1
        A = list(set(A))
        A.sort()
        res = 1
        i = 0
        while i < len(A) and A[i] <= 0:
            i += 1
        while i < len(A) :
            if A[i] != res:
                return res
            else:
                res += 1
                i += 1
        return res