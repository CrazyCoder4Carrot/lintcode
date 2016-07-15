class Solution:
    # @param nums: A list of non-negative integers.
    # return: an integer
    def houseRobber2(self, nums):
        # write your code here
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        even = nums[0]
        odd = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            if i % 2 == 0:
                even = max(odd, even + nums[i])
            else:
                odd = max(even, odd + nums[i])
        res1 = max(odd, even)
        odd = nums[1]
        even = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            if i % 2 == 0:
                even = max(odd, even + nums[i])
            else:
                odd = max(even, odd + nums[i])
        res2 = max(odd, even)
        return max(res1, res2)
        