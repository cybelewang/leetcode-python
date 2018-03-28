"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        n, diff = len(prices), []
        for i in range(1, n):
            diff.append(prices[i] - prices[i-1])

        gain = [0]*(n-1)
        gain[0] = max(gain[0], diff[0])
        for i in range(1, min(3, n-1)):
            gain[i] = max(gain[i-1], diff[i])

        for i in range(3, n-1):
            if diff[i] < 0:
                gain[i] = gain[i-1]
            else:
                if diff[i-1] < 0:
                    gain[i] = max(gain[i-1], gain[i-3] + diff[i])
                else:
                    gain[i] = max(gain[i-1], gain[i-3]) + diff[i]

        return gain[-1]

test_case = [1, 101, 99, 102]
obj = Solution()
print(obj.maxProfit(test_case))
