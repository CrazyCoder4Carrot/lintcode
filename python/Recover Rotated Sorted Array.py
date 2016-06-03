class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    241ms
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        i = 0
        while i + 1 < len(nums):
            if nums[i] <= nums[i + 1]:
                i += 1
            else:
                i += 1
                break
        if i == len(nums) - 1:
            return
        temp = nums[:i]
        j = 0
        while j < i and i < len(nums):
            nums[j] = nums[i]
            j += 1
            i += 1
        while j < len(nums):
            nums[j] = temp[j - i]
            j += 1