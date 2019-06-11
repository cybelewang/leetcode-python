"""
123 Best Time to Buy and Sell Stock III

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

    # 2nd round solution on 6/11/2019
    def maxProfit2(self, prices):
        N = len(prices)
        if N < 2:
            return 0
        
        # left[i] is the max profit with up to ONE transaction on previous i days
        # right[i] is the max profit with up to ONE transaction on last i days
        left, right = [0]*(N+1), [0]*(N+1)
        low = prices[0]
        for i in range(1, N):
            left[i+1] = max(left[i], prices[i] - low)
            low = min(low, prices[i])

        high = prices[N-1]
        for i in range(N-1, -1, -1):
            right[N-i] = max(right[N-i-1], high - prices[i])
            high = max(high, prices[i])
        
        res = 0
        for i in range(N+1):
            res = max(res, left[i] + right[N-i])
        
        return res

obj = Solution()
test_cases = [[], [100], [7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]
for case in test_cases:
    print(obj.maxProfit2(case))