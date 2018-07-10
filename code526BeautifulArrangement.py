"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully 
if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Note:
N is a positive integer and will not exceed 15.
"""
class Solution:
    # https://leetcode.com/problems/beautiful-arrangement/discuss/99738/Easy-Python-~230ms
    # X is the set of still available numbers.
    # Note that my i goes downwards, from N to 1. Because position i = 1 can hold any number, so I don't even have to check whether the last remaining number fits there. 
    # Also, position i = 2 happily holds every second number and i = 3 happily holds every third number, so filling the lowest positions last has a relatively high chance of success. 
    # In other words, it's relatively hard to end up with dead ends this way.
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def count(i, X):
            if i == 1:
                return 1
            return sum(count(i - 1, X - {x})
                    for x in X
                    if x % i == 0 or i % x == 0)

        return count(N, set(range(1, N + 1)))
    # brutal force recursive solution
    # note, we don't need to build the beautiful arrays
    def countArrangement2(self, N):
        """
        :type N: int
        :rtype: int
        """
        def dfs(nums, used, start):
            if start == N+1:
                return 1
            res = 0
            for i in range(1, N+1):
                if not used[i] and (nums[i] % start == 0 or start % nums[i] == 0):
                    used[i] = True
                    res += dfs(nums, used, start+1)
                    used[i] = False

            return res

        nums = list(range(N+1)) # nums[i] = i
        used = [False]*(N+1)

        return dfs(nums, used, 1)

print(Solution().countArrangement2(4))