class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        mapdict = {}
        for i in range(len(numbers)):
            if (target - numbers[i]) in mapdict:
                return [mapdict[target - numbers[i]] + 1, i + 1]
            else:
                mapdict[numbers[i]] = i
        return [-1, - 1]