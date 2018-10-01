"""
754 Reach a Number

You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].
"""
from math import ceil, sqrt
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/8456022.html
    # trick 1: -target and target have the same steps
    # trick 2: assume a step is n and the n*(n+1)//2 is the first sum that larger or equal to target, then the difference between n*(n+1)//2 and target is d (positive)
    # then if d is even, we just need to adjust the sign of d//2 step to negative
    # if d is odd, we 
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        n = ceil((-1.0 + sqrt(1.0 + 8.0*target))/2)

        sum = n*(n+1)//2
        if sum == target:
            return n
        
        diff = sum - target
        if diff & 1 == 0:
            return n
        else:
            return n + 2 if n & 1 else n + 1

print(Solution().reachNumber(4))