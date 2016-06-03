class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        if not nums1 or not nums2:
            return []
        minval = min(min(nums1), min(nums2))
        maxval = max(max(nums1), max(nums2))
        mapdict = [0] * (maxval - minval + 1)
        res = []
        for val in nums1:
            mapdict[val - minval] += 1
        for val in nums2:
            if mapdict[val - minval] > 0 :
                res.append(val)
                mapdict[val - minval] -= 1
        return res
        