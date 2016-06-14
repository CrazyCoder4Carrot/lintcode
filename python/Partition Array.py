class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if not nums:
            return 0
        start, end = 0, len(nums) - 1
        while start < len(nums) and nums[start] < k:
                start += 1
        while start <= end:
            if nums[start] >= k:
                while end >= 0 and nums[end] >= k :
                    end -= 1
                if end <= start:
                    break
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            else:
                start += 1
        return start