class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def rotate(self, matrix):
        if not matrix:
            return None
        res = []
        for y in range(len(matrix[0]))[::-1]:
            temp = []
            for x in range(len(matrix)):
                temp.append(matrix[x][y])
            res.append(temp)
        return res
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix[0]
            matrix = self.rotate(matrix[1:])
        return res