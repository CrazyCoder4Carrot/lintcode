class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        num = 0
        for i in range(len(A)):
            if A[i] != elem:
                A[num] = A[i]
                num += 1
        return num