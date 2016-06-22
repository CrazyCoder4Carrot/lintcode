class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        self.quicksort(A, 0, len(A) - 1)
    def quicksort(self, A, lo, hi):
        if lo >= hi:
            return
        p = self.partition(A, lo, hi)
        self.quicksort(A, lo, p-1)
        self.quicksort(A, p+1, hi)
    def partition(self, A, lo, hi):
        key = A[hi]
        i = lo - 1
        for j in range(lo, hi):
            if A[j] < key:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[hi] = A[hi], A[i+1]
        return i + 1