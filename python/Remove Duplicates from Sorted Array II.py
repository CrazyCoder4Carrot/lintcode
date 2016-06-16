class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if not A or len(A) < 3:
            return 0
        end = 1
        for i in range(2, len(A)):
            if A[i] != A[end - 1]:
                end += 1
                A[end] = A[i]
        return end + 1
            