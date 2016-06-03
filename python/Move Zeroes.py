class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[i - count] = nums[i]
        while count > 0 :
            nums[len(nums) - count] = 0
            count -= 1
        return nums