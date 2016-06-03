class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        maxval = max(nums)
        minval = min(nums)
        mapkeys = [0] * (maxval - minval + 1)
        maxcount = 0
        maxkey = 0
        for val in nums:
            mapkeys[val - minval] += 1
            if mapkeys[val - minval] > maxcount:
                maxcount = mapkeys[val - minval]
                maxkey = val
        return maxkey