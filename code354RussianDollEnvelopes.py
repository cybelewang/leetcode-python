"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). 
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
# similar problem: 300, Longest Increasing Subsequence
from bisect import bisect_left
class Solution:
    # 1. sort the envelopes with the following rule: first compare width, smaller width in left. If same width, the bigger height in left.
    # 2. after sorting, find the longest increasing subsequence in the heights list
    # http://www.cnblogs.com/grandyang/p/5568818.html
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key = lambda x: (x[0], -x[1]))

        doll = [0]*len(envelopes)
        maxLen = 0

        for envelope in envelopes:
            i = bisect_left(doll, envelope[1], 0, maxLen)
            doll[i] = envelope[1]
            if i == maxLen:
                maxLen += 1

        return maxLen
            
    # O(n^2), TLE
    def maxEnvelopes2(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n < 1:
            return 0

        envelopes.sort()
        dp = [1]*n
        res = 0

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if envelopes[j][1] < envelopes[i][1] and envelopes[j][0] < envelopes[i][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    # below is wrong because the right-most one may not be the max one, for example [[46,89],[50,53],[52,68],[72,45],[77,81]]
                    # dp[i] = 1 + dp[j]
                    # break
            res = max(res, dp[i])
        
        return res

envelopes = [[46,89],[50,53],[52,68],[72,45],[77,81]]
obj = Solution()
print(obj.maxEnvelopes(envelopes))