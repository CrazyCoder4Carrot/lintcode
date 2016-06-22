class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here
        for i in range(1, len(A)):
            j = i - 1
            key = A[i]
            while j >= 0 and A[j] > key:
                A[j+1] = A[j]
                j -= 1
            A[j + 1] = key