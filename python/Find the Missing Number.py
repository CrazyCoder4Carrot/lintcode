class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        # write your code here
        nums.sort()
        return ((len(nums) + 1))* (len(nums))/2 - sum(nums)
        