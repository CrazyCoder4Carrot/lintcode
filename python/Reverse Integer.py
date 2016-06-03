class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        flag = ""
        if n < 0 :
            flag = "-"
            n = -n
        res = int(flag + str(n)[::-1])
        return  res if res < 2 ** 32 else 0