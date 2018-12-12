"""
188 Best Time to Buy and Sell Stock IV

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k < 1:
            return 0

        n = len(prices)
        if k >= n//2:
            return self.quickSolve(prices)

        t = [[0 for j in range(n)] for i in range(k+1)] # t[i][j] means the max profit up to ith transactions and up to jth day 
        for i in range(1, k+1):
            tempMin = prices[0] - 0 # tempMin = cost - previous profit, or current transaction's overall cost
            for j in range(1, n):
                t[i][j] = max(t[i][j-1], prices[j] - tempMin)   # option 1: no sell transaction on day j, option 2: sell transaction on day j. Selling action is part of current transaction, so we don't need to increase i
                tempMin = min(tempMin, prices[j] - t[i-1][j-1]) # option 1: no buy transaction on day j, option 2: buy transaction on day j. Buying action is a start of a transaction, so it must be based on previous transaction, that's why we use t[i-1][j-1]

        #print(t)
        return t[k][n-1]

    def quickSolve(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit


test_price = [7, 1, 5, 3, 6, 4, 9, 1]
obj = Solution()
print(obj.maxProfit(3,test_price))