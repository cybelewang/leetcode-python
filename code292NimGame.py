"""
292 Nim Game

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
"""
class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n%4 != 0)


'''         if n < 4:#check this corner case
            return True

        win = [True]*(n+1)
        for i in range(4, n+1):
            win[i] = not(win[i-3] and win[i-2] and win[i-1])

        return win[n] '''

obj = Solution()
for i in range(10):
    print(i, obj.canWinNim(i), sep = '->')

"""
generalize一下这道题，当可以拿1～n个石子时，那么个数为(n+1)的整数倍时一定会输
http://www.cnblogs.com/grandyang/p/4873248.html
"""