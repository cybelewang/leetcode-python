"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        
        # Find the pivot index
        rotated = False
        n = len(nums)
        for j in range(1, n):
            if nums[j] < nums[j-1]:
                rotated = True
                break
        
        l, r = 0, n - 1
        if rotated:
            l = j
            r = j - 1 + n   # extended index, when e == n, it actually points to 0
        
        # Now do binary search with extended index range
        while l <= r:
            mid = (l + r) // 2
            actual = mid if mid < n else mid - n

            if nums[actual] == target:
                return True
            elif nums[actual] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False 
        
test_case = [4, 4, 4, 4, 0, 1, 2, 4]
obj = Solution()
print(obj.search(test_case, 0))
        