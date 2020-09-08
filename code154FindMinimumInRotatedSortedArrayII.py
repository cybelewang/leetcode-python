"""
154 Find Minimum in Rotated Sorted Array II

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""
import unittest
class Solution:
    # OJ solution, average O(logN), worst O(N)
    def findMin(self, nums):
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
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

    # follow-up: find the maximum in rotated sorted array, the array may contain duplicates
    # find the pivot point that nums[i] > nums[i+1], we can do this with binary search
    def findMax(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]: return nums[r] # sorted subarray, not rotated
            # because l < r, l <= mid < r          
            mid = (l + r) // 2
            # check if mid is the pivot point
            if nums[mid] > nums[mid + 1]: return nums[mid]
            # # [mid] and [mid+1] are not pivot pair, search left or right by comparing [mid] and [r]
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        
        return nums[l]

    # similar generic binary search solution to find the pivot 
    # here we are looking for the minimum value, so we compare nums[mid] with nums[mid-1]
    def findMin3(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]: return nums[l] # sorted subarray, not rotated
            mid = (l + r) // 2
            # check if nums[mid-1] > nums[mid], if so, nums[mid] is the result
            if mid > 0 and nums[mid] < nums[mid-1]: return nums[mid]
            # [mid-1] and [mid] are not pivot pair, search left or right by comparing [mid] and [r]
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
        
        return nums[l]

class Test(unittest.TestCase):
    def test1(self):
        # a few duplicates
        test_case = [2, 4, 5, 6, 7, 7, 0, 0, 1, 2]
        obj = Solution()
        self.assertEqual(obj.findMin(test_case), 0)
        self.assertEqual(obj.findMax(test_case), 7)
    def test2(self):
        # a lot duplicates
        test_case = [0, 1, 1, 1, 1, 0, 0]
        obj = Solution()
        self.assertEqual(obj.findMin(test_case), 0)
        self.assertEqual(obj.findMax(test_case), 1)
        test_case = [0, 0, 0, 1, 1, 0, 0]
        self.assertEqual(obj.findMin(test_case), 0)
        self.assertEqual(obj.findMax(test_case), 1)

if __name__ == '__main__':
    unittest.main(exit = False)