"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). 
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n < 1:
            return 0

        envelopes.sort(key = lambda x: (x[0], x[1]))
        dp = [1]*n

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if envelopes[j][1] < envelopes[i][1] and envelopes[j][0] < envelopes[i][0]:
                    dp[i] = 1 + dp[j]
                    break
        
        return max(dp)

envelopes = [[46,89],[50,53],[52,68],[72,45],[77,81]]
obj = Solution()
print(obj.maxEnvelopes(envelopes))