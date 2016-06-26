class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        res = []
        S.sort()
        self.search(S, [], 0, res)
        return res
    def search(self, nums, temp, index, res):
        if index == len(nums):
            res.append(temp)
            return
        self.search(nums, temp + [nums[index]], index + 1, res)
        self.search(nums, temp, index + 1, res)
        