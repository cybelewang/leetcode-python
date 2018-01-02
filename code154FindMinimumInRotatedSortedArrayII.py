"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""

# have to search min linearily, compare [1, 0, 1, 1, 1, 1, 1] and [1, 1, 1, 1, 1, 0, 1], there is no way to tell if we need to search left half or right half
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 0, len(nums)
        for i in range(1, n+1):
            if nums[i%n] < nums[i-1]:
                break
        
        return nums[i%n]

test_case = [1, 1, 1, 1, 1, 0, 1]
obj = Solution()
print(obj.findMin(test_case))