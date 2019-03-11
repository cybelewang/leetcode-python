"""
949 Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""

Note:

A.length == 4
0 <= A[i] <= 9
"""
from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ans = -1
        for h1, h2, m1, m2 in permutations(A):
            hours = h1*10 + h2
            mins = m1*10 + m2
            time = hours*60 + mins
            if hours < 24 and mins < 60 and time > ans:
                ans = time
        
        if ans == -1:   return ""
        return "{:02}:{:02}".format(*divmod(ans, 60))

A = [1,2,3,4]
print(Solution().largestTimeFromDigits(A))