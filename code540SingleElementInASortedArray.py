"""
540 Single Element in a Sorted Array

Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.

"""
class Solution:
    # my own binary search solution
    # before the single element, the array should be like [1, 1, 2, 2] where [even] == [even + 1]
    # after the single element, the array should be like [1, 2, 2] where [even] != [even + 1]
    # |e|o| |e|o| ... |s| |o|e| |o|e|    
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j)//2
            if mid & 0x01:
                # mid is odd
                if nums[mid-1] == nums[mid]:
                    # left half is good, search right half
                    i = mid + 1
                else:
                    # left half contains the single element
                    j = mid - 1
            else:
                # mid is even
                # note i < j, so mid < j, and mid + 1 < len(nums) - 1
                if nums[mid] == nums[mid+1]:
                    # left half and this pair is good, search from next pair
                    i = mid + 2
                else:
                    # left half contains the single element
                    j = mid
        
        return nums[i]

nums = [1, 2, 2]
print(Solution().singleNonDuplicate(nums))