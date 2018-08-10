"""
You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, 
where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
Example 3:
Input: [1,2,3,4,4,5]
Output: False
Note:
The length of the input is in range of [1, 10000]
"""
from collections import defaultdict
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/7525821.html
    # greedy solution, use two maps: freq and need
    # 
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq, need = defaultdict(int), defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        for num in nums:
            if freq[num] == 0:
                continue
            elif need[num] > 0:
                need[num] -= 1
                need[num+1] += 1
            elif freq[num+1] > 0 and freq[num+2] > 0:
                freq[num+1] -= 1
                freq[num+2] -= 1
                need[num+3] += 1
            else:
                return False
            
            freq[num] -= 1
        
        return True

nums= [1, 2, 3, 3, 4, 5]
print(Solution().isPossible(nums))