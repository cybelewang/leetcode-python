"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""
# similar problems: 518
class Solution:
    # DP solution, accepted
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount < 0:
            return -1

        dp = [1 + amount]*(1 + amount)
        dp[0] = 0

        for i in range(1, 1+amount):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i-coin])

        return -1 if dp[amount] == 1 + amount else dp[amount]

    # my own solution. wrong, see coins [186,419,83,408] and amount 6249
    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount < 0:
            return -1

        if amount == 0:
            return 0

        coins.sort()
        res = 2**31 - 1
        for i in range(len(coins)-1, -1, -1):
            num, remain = amount//coins[i], amount%coins[i]
            j = i - 1
            while j > -1 and remain > 0:
                num += remain//coins[j]
                remain %= coins[j]
                j -= 1
            
            if remain == 0:
                res = min(res, num)
        
        return res if res != 2**31 -1 else -1

coins = [1, 2, 5]
amount = 11
obj = Solution()
print(obj.coinChange(coins, amount))