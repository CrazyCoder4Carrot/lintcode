class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        start = 0
        end = len(nums) - 1
        while start < end:
            while(nums[start] % 2 != 0):
                start += 1
            while(nums[end] % 2 == 0):
                end -= 1
            if start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return 