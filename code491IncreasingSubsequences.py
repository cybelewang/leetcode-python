"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
"""
# similar problems: 90 Subsets II
from collections import defaultdict
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/6388103.html, solution 4
    # a solution without using set: use a dict to save the number's "cur" length, default to 0 (beginning)
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, cur = [], [[]] # cur is the growing list with all intermediate lists, intially there is an empty list, so numbers can be inserted to it
        mem = defaultdict(int)
        for num in nums:
            n = len(cur)
            start = mem[num]
            mem[num] = n
            for j in range(start, n):
                if cur[j] and cur[j][-1] > num:
                    continue
                cur.append(cur[j][:])   # bug fixed: don't forget the "copy" [:]
                cur[-1].append(num)
                if len(cur[-1]) >= 2:
                    res.append(cur[-1])
            
        return res

obj = Solution()
nums = [4, 6, 7, 7]
print(obj.findSubsequences(nums))