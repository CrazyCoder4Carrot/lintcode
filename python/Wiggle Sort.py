class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        # Write your code here
        if not nums:
            return nums
        for i in range(1, len(nums)):
            if (i % 2 == 0 and nums[i] > nums[i-1]) or (i % 2 != 0 and nums[i] < nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]
        return