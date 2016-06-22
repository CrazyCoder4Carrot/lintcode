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


class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        b = self.merge_sort(A)
        for i in range(len(b)):
            A[i] = b[i]
    def merge_sort(self, a):
        if len(a) <= 1:
            return a
        mid = (0 + len(a))/2
        l1 = self.merge_sort(a[:mid])
        l2 = self.merge_sort(a[mid:])
        l3 = self.merge(l1, l2)
        return l3
    def merge(self, a, b):
        if not a :
            return b
        if not b:
            return a
        i, j = 0, 0
        c = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        while i < len(a):
            c.append(a[i])
            i += 1
        while j < len(b):
            c.append(b[j])
            j += 1
        return c