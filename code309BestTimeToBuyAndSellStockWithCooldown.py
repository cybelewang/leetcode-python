"""
309 Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""
# https://soulmachine.gitbooks.io/algorithm-essentials/java/dp/best-time-to-buy-and-sell-stock-with-cooldown.html
# two dp arrays
# sell[i] is the max profit when there is no stock on the ith day
# buy[i] is the max profit when there is stock on the ith day
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        n = len(prices)
        if n < 2:
            return 0

        buy, sell = [0]*n, [0]*n
        buy[0], buy[1] = -prices[0], -min(prices[0:2])
        sell[1] = max(0, buy[0] + prices[1])
        for i in range(2, n):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])

        return sell[-1]


test_case = [1, 101, 99, 102]
obj = Solution()
print(obj.maxProfit(test_case))
