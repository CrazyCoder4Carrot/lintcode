class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        if not A:
            return 0
        if len(A) == 1:
            return A[0]
        nums = [0] * len(A)
        nums[0] = A[0]
        nums[1] = max(nums[0], A[1])
        for i in range(2, len(A)):
            if A[i] + nums[i-2] > nums[i-1]:
                nums[i] = A[i] + nums[i-2]
            else:
                nums[i] = nums[i-1]
        return nums[-1]