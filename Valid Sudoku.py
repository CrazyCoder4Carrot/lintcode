class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def validate(self, temp):
        mapdict = {}
        for val in temp:
            if val not in mapdict:
                mapdict[val] = 1
            else:
                mapdict[val] += 1
        for val in range(0,10):
            if str(val) in mapdict and mapdict[str(val)] > 1:
                return False
        return True
    def isValidSudoku(self, board):
        if not board:
            return False
        if len(board) != 9:
            return False
        if len(board[0]) != 9:
            return False
        for i in range(0, 9):
            if not self.validate(board[i]):
                return False
        for i in range(0, 9):
            temp = []
            for j in range(0, 9):
                temp.append(board[j][i])
            if not self.validate(temp):
                return False
        for i in range(0,3):
            for j in range(0, 3):
                temp = []
                for x in range(0,3):
                    for y in range(0, 3):
                        temp.append(board[i * 3 + x][j * 3 + y])
                if not self.validate(temp):
                    return False
        return True