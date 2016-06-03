class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0
        maxsofa = prices[-1]
        profit = 0
        i = len(prices) - 2
        while i >=0:
            if maxsofa - prices[i] > profit:
                profit = maxsofa - prices[i]
            if prices[i] > maxsofa:
                maxsofa = prices[i]
            i-= 1
        return profit

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0
        low = prices[0]
        profit = 0
        for price in prices[1:]:
            if price - low > profit :
                profit = price - low
            if price < low:
                low = price
        return profit