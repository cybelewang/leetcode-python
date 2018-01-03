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
    # OJ solution
    def findMin(self, nums):
        l = 0
        h = len(nums)-1
        while l<h:
            mid = int((l+h)//2)
            if nums[mid] > nums[h]:
                l = mid+1
            elif nums[mid] < nums[h]:
                h = mid
            else:
                h -= 1
        return nums[l]
    
    # O(n) solution
    def findMin2(self, nums):
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