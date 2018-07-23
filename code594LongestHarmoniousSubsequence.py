"""

We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
"""
# similar problems: 560 Subarray Sum Equals k
from collections import defaultdict
class Solution:
    # my own solution
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(int)
        res = 0
        for i in nums:
            val = count[i] + 1
            count[i] = val
            res = max(res, val + count[i-1], val + count[i+1])

        return res

nums = [1,3,2,2,5,2,3,7]
print(Solution().findLHS(nums))
