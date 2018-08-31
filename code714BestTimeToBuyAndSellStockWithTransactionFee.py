"""
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. 
You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""
# similar problems: 123, 188, 309
class Solution:
    # solution 2 from http://www.cnblogs.com/grandyang/p/7776979.html
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        sold, hold = 0, -prices[0]
        for price in prices:
            t = sold
            sold = max(sold, hold + price - fee)
            hold = max(hold, t - price)
        
        return sold
        
    # my own solution using knapsack algorighm, TLE
    def maxProfit_TLE(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        dp = [0]*n
        for i in range(1, n):
            dp[i] = dp[i-1] # no selling on day i
            for j in range(i):  # selling on day i, need to iterate previous days and get the max profit
                dp[i] = max(dp[i], dp[j] + prices[i] - prices[j] - fee)
        
        return dp[-1]

prices, fee = [1, 3, 2, 8, 4, 9], 2
print(Solution().maxProfit(prices, fee))