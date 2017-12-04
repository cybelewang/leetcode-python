"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
# divide the list to two parts [0:i] and [i:n-1] for different i in range(0, n)
# for each part, find the max profit
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        
        n = len(prices)

        leftMaxProfit, rightMaxProfit = [0]*n, [0]*n
        low, high = prices[0], prices[-1]

        for (i, num) in enumerate(prices):
            # get the max profit for prices[0 to i]
            if i > 0:
                leftMaxProfit[i] = max(leftMaxProfit[i-1], num - low)
            if num < low:
                low = num
            
            # get the max profit for prices[n-1 to i]
            if i > 0:
                rightMaxProfit[n- 1 - i] = max(rightMaxProfit[n - i], high - prices[n - 1 - i])

            if prices[n - 1 - i] > high:
                high = prices[n - 1 - i]
                
        # Now traversal the sum of leftMaxProfit and rightMaxProfit and get the result
        res = 0
        for i in range(n):
            res = max(res, leftMaxProfit[i] + rightMaxProfit[i])
        
        return res

obj = Solution()
test_cases = [[], [100], [7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]
for case in test_cases:
    print(obj.maxProfit(case))