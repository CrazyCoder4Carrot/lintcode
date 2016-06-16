class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        if not A:
            return 0
        if len(A) == 1 or len(A) == 2:
            return len(A)
        maxval = 2
        count = 2
        inc = True if A[1] > A[0] else False
        for i in range(2, len(A)):
            if A[i] > A[i-1]:
                if inc:
                    count += 1
                    if count > maxval:
                        maxval = count
                else:
                    count = 2
                    inc = True
            if A[i] < A[i-1]:
                if not inc:
                    count += 1
                    if count > maxval:
                        maxval = count
                else:
                    count = 2
                    inc = False
        return maxval