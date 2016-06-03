class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
	    # write you code here
	    if not s:
	        return s
	    offset = offset % len(s)
	    for i in range(offset):
	        temp = s[-1]
	        for j in range(1, len(s))[::-1]:
	            s[j] = s[j - 1]
	        s[0] = temp