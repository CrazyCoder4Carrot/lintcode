class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j-1]
                else:
                    if j == 0 and i > 0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        if i > 0 and j > 0:
                            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
            