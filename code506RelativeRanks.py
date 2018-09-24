"""
506 Relative Ranks

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, 
who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
"""
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        t = sorted(zip(nums, range(len(nums))), reverse = True)
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        for i, (_, index) in enumerate(t):
            if i < 3:
                nums[index] = medals[i]
            else:
                nums[index] = str(i+1)
        
        return nums

nums = [5, 4, 1, 2, 3]
print(Solution().findRelativeRanks(nums))
