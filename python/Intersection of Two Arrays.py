"""
844ms
"""
class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        return list(set(nums1).intersection(set(nums2)))


"""
697ms
Using two sets
"""
class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        #Write your code here
        res = set()
        set1 = set(nums1)
        set2 = set(nums2)
        for val in set1:
            if val in set2:
                res.add(val)
        return list(res)
"""
using map
1114 ms
"""
class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        #Write your code here
        res = set()
        if not nums1 or not nums2:
            return []
        low1 = min(nums1)
        low2 = min(nums2)
        hi1 = max(nums1)
        hi2 = max(nums2)
        low = low1 if low1 < low2 else low2
        high = hi1 if hi1 > hi2 else hi2
        maparr = [0] * (high - low + 1)
        for val in nums1:
            maparr[val - low] += 1
        for val in nums2:
            if maparr[val - low] > 0:
                res.add(val)
        return list(res)