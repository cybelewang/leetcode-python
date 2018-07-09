"""

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1
"""
# similar problems: 322, 377
# initially thought to use 264 Ugly Number II's method, but that one cannot be used here
# the key idea here is to iterate all combinations without overlapping
class Solution(object):
    # help from http://www.cnblogs.com/grandyang/p/7669088.html
    # dp[i] is number of combinations for amount i
    # first iterate coin, then for each coin add all possible amount
    # for loop sequence is different from 1st trial
    # this is a 1-D space DP solution, it can be derived from knapsack method, which uses 2-D space:
    # https://leetcode.com/problems/coin-change-2/discuss/99212/Knapsack-problem-Java-solution-with-thinking-process-O(nm)-Time-and-O(m)-Space
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0]*(amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]

        return dp[amount]
        
    # 1st trial, wrong solution, overlapping cases
    def change_Wrong(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0]*(amount+1)
        dp[0] = 1

        coins.sort()

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin > -1:
                    dp[i] += dp[i-coin]

        return dp[amount]

amount = 5
coins = [1, 2, 5]
print(Solution().change(amount, coins))