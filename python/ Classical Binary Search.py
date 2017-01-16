class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # Write your code here
        def binarySearch(low, high, target, A):
            if low < high:
                mid = (low + high) / 2
                if target == A[mid]:
                    return mid
                if target < A[mid]:
                    return binarySearch(low, mid - 1, target, A)
                if target > A[mid]:
                    return binarySearch(mid + 1, high, target, A)
            else:
                return -1
        return binarySearch(0, len(A) - 1, target, A)
