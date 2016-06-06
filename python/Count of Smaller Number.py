
class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        mapdict1 = [0] * 10001
        mapdict2 = [0] * 10001
        res = []
        for val in A:
            mapdict1[val] = mapdict1[val] + 1 if mapdict1[val] != 0 else 1
        count = 0
        for i in range(1, len(mapdict2)):
            mapdict2[i] = mapdict2[i-1] + mapdict1[i-1]
        for val in queries:
            res.append(mapdict2[val])
        return res
            


class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        A.sort()
        res = []
        for val in queries:
            res.append(self.findSN(A, val))
        return res
    def findSN(self, A, target):
        if len(A) == 0 or A[-1] < target:
            return len(A)
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] <  target:
                start = mid
            else:
                end = mid
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return end + 1
                
            