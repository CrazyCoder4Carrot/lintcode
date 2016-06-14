class Solution:
    """
    @param n: n
    @param k: the k-th permutation
    @return: a string, the k-th permutation
    """
    def getPermutation(self, n, k):
        string = str("".join(map(str, range(1, n + 1))))
        res = []
        self.helper(string, len(string), "", res)
        return res[k-1]
    def helper(self, string, count, temp, res):
       if len(temp) == count:
           res.append(temp)
           return
       else:
           for i in range(len(string)):
               self.helper(string[:i] + string[i+1:], count, temp + string[i], res)