class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        if not matrix:
            return
        flag = False
        if 0 in matrix[0]:
            flag = True
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])-1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if flag:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
                