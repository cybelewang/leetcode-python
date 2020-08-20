"""
1423 Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain. 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 
Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
 
Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""
class Solution:
    # the problem can be transformed to find min sum of fixed size (n-k) subarray
    # sliding window solution, time O(N)
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        su, minSum = 0, 2**31 - 1
        for i in range(n):
            su += cardPoints[i]
            if i+1 > n-k:
                su -= cardPoints[i+k-n]
            if i+1 >= n-k:
                minSum = min(minSum, su)
        
        return sum(cardPoints) - minSum    
    
    # DP solution, time O(K^2), TLE
    def maxScore_DP(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        dp = [[0]*(k+1) for _ in range(k+1)]
        for t in range(1, k+1):
            for l in range(t+1):
                right = dp[t-1][l] + cardPoints[n-t+l] if l <= t-1 else -2**31
                left = dp[t-1][l-1] + cardPoints[l-1] if l >= 1 else -2**31
                dp[t][l] = max(left, right)
        
        return max(dp[k])

    # G follow-up: if there is another weight list, find the max sum of the k picked numbers from two ends, need to use corresponding weight
    # Use the above DP method