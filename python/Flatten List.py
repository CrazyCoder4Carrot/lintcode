class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def __init__(self):
        self.res = []
    def flatten(self, nestedList):
        # Write your code here
        if isinstance(nestedList, int):
            self.res.append(nestedList)
        else:
            self.helper(nestedList)
        return self.res
    def helper(self, nestedList):
        for item in nestedList:
            if isinstance(item, int):
                self.res.append(item)
            else:
                self.helper(item)