"""
81 Search in Rotated Sorted Array II

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
    # 2nd round solution on 6/16/2019
    # https://www.cnblogs.com/grandyang/p/4325840.html
    def search2(self, nums, target):    
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[r]:
                # right half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[r]:
                # left half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # don't know the trend, just decrease r to next loop
                r -= 1
        
        return False


test_case = [4, 4, 4, 4, 0, 1, 2, 4]
obj = Solution()
print(obj.search2(test_case, 0))
        