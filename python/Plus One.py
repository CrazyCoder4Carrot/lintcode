"""
str convert to int
571 ms
"""

class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        return map(int, list(str(int("".join(map(str, digits))) + 1)))
"""
simulation 
555 ms
"""

class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        flag = 0
        i = len(digits) - 1
        while i >= 0:
            if i == len(digits) - 1:
                if digits[i] + 1 < 10:
                    digits[i] += 1
                    flag = 0
                else:
                    digits[i] = digits[i] + 1 - 10
                    flag = 1
            else:
                if digits[i] + flag < 10:
                    digits[i] += flag
                    flag = 0
                else:
                    digits[i] = digits[i] + flag - 10
                    flag = 1
            i -= 1
        if flag:
            digits.insert(0,1)
        return digits