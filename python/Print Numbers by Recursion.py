class Solution:
    # @param n: An integer.
    # return : A list of integer storing 1 to the largest number with n digits.
    def numbersByRecursion(self, n):
        # write your code here
        if not n:
            return []
        res = self.helper(n)
        return res[1:]
    def helper(self, n):
        res = []
        if n == 1:
            res += [i for i in range(0, 10)]
            return res
        temp = self.helper(n-1)
        res += temp
        for i in range(1, 10):
            res += [num + 10 ** (n-1) *i for num in temp]
        return res