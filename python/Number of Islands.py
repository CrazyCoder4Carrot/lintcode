class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        island = 0
        if not grid:
            return island 
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                  queue.append((i,j))
                  while queue:
                      x, y = queue.pop(0)
                      grid[x][y] = 0
                      if x + 1 < len(grid) and grid[x+1][y] == 1:
                          queue.append((x+1, y))
                      if x -1 >= 0 and grid[x-1][y] == 1:
                          queue.append((x-1, y))
                      if y - 1 >= 0 and grid[x][y-1] == 1:
                          queue.append((x, y - 1))
                      if y + 1 < len(grid[0]) and grid[x][y+1] == 1:
                          queue.append((x, y + 1))
                  island += 1
        return island