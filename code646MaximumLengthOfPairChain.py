"""
646 Maximum Length of Pair Chain

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].
"""
class Solution:
    # my own solution, sort pairs naturally, then use greedy to extend or shrink the end
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()

        pre_end = pairs[0][1]
        res = 1
        for i in range(1, len(pairs)):
            s, e = pairs[i]
            if s > pre_end:
                pre_end = e
                res += 1
            else:
                pre_end = min(pre_end, e)

        return res

    # 2nd round solution on 7/1/2020
    # sort pairs based on the second number, this guarantees pair will be selected with small end first, 
    # then we can use greedy to count the max chains.
    # https://www.cnblogs.com/grandyang/p/7381633.html
    def findLongestChain2(self, pairs):
        pairs.sort(key=lambda p: (p[1], p[0]))
        end, res = pairs[0][1], 1
        for s, e in pairs:
            if s > end:
                res += 1
                end = e
        
        return res

pairs = [[1,2], [2,4], [3,4]]
print(Solution().findLongestChain2(pairs))