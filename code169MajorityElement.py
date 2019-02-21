"""
169 Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
# Similar problems: 229 Majority Element II
class Solution:
    # Moore majority vote algorithm https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, i = nums[0], 1
        for x in nums[1:]:            
            if i == 0:
                m, i = x, 1
            elif m == x:
                i += 1
            else:
                i -= 1
        
        return m

test_case = [1, 2, 3, 2, 2, 3]
obj = Solution()
print(obj.majorityElement(test_case))