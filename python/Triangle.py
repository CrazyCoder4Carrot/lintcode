class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    313 ms
    """
    def minimumTotal(self, triangle):
        # write your code here
        i = len(triangle) - 2
        while i >= 0:
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1]) 
            i -= 1
        return triangle[0][0]