"""
948 Bag of Tokens

You have an initial power P, an initial score of 0 points, and a bag of tokens.

Each token can be used at most once, has a value token[i], and has potentially two ways to use it.

If we have at least token[i] power, we may play the token face up, losing token[i] power, and gaining 1 point.
If we have at least 1 point, we may play the token face down, gaining token[i] power, and losing 1 point.
Return the largest number of points we can have after playing any number of tokens.


Example 1:

Input: tokens = [100], P = 50
Output: 0
Example 2:

Input: tokens = [100,200], P = 150
Output: 1
Example 3:

Input: tokens = [100,200,300,400], P = 200
Output: 2
 

Note:

tokens.length <= 1000
0 <= tokens[i] < 10000
0 <= P < 10000
"""
class Solution:
    # my own solution
    # sort tokens first, then trying to subtract tokens from smallest, until P < next smallest token
    # once P < next smallest token, we add the largest toaken to P by consuming 1 point, and then repeat above process
    # a pitfall is the final points may not be the result because we may consume a point to take the last remaining token
    # for example, tokens = [100, 200], P = 100, the result is 1 but the final point is 0
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        i, j, points, res = 0, len(tokens) - 1, 0, 0
        while i <= j:
            if P >= tokens[i]:
                # consume P first
                P -= tokens[i]
                i += 1
                points += 1
                res = max(res, points)
            elif points > 0:
                # if P is not enough, consume points
                P += tokens[j]
                j -= 1
                points -= 1                
            else:
                # if both P and points are not enough, stop here 
                break
        
        return res

tokens = [100,200]
P = 100
print(Solution().bagOfTokensScore(tokens, P))