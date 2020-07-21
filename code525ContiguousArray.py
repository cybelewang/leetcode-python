"""
525 Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

"""
# similar problems: 523
class Solution:
    # my own solution
    # use a dict to save the difference (number difference between 1s and 0s) and corresponding index i
    # later if the same diff is seen in index j, then j - i will be a length that meets the requirement
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, mem, diff = 0, {0:-1}, 0
        for i, num in enumerate(nums):
            if num != 0:
                diff += 1
            else:
                diff -= 1

            if diff in mem:
                res = max(res, i - mem[diff])
            else:
                mem[diff] = i
        
        return res

    # another O(N^2) method: count 1s ending with nums[i], name it ones[i]. Then we put ones[i] and i into hashmap. 
    # Then we iterate to index j and find count[j] - count[i] = (j-i)//2, we find a pair (i, j)

nums = [0,0]
print(Solution().findMaxLength(nums))
