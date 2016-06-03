class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        return map(int, list(str(int("".join(map(str, digits))) + 1)))