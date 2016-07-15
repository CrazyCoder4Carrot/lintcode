class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        res = index = gasres =  0
        for i in range(len(gas)):
            res += gas[i] - cost[i]
            if gasres < 0:
                index = i
                gasres = 0
            gasres += gas[i] - cost[i]
        return index if res >=0 else -1