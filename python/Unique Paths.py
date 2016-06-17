class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        if m < 0 or n < 0:
            return 0
        res = [0] * n
        res[0] = 1
        for i in range(m):
            for j in range(1, n):
                res[j] += res[j-1]
        return res[-1]