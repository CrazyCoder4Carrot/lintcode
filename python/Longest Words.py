class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        dictionary.sort(key = lambda x: len(x), reverse = True)
        length = len(dictionary[0])
        return filter(lambda x: len(x) == length, dictionary)