class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        i = -1
        for j in range(0, len(chars)):
            if chars[j].islower():
                i += 1
                chars[i], chars[j] = chars[j], chars[i]