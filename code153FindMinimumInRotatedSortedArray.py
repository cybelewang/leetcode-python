"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        i, j = 0, len(nums)-1
        while i < j and nums[i] > nums[j]:
            m = (i + j)//2
            if nums[i] > nums[m]:
                i += 1
                j = m
            else:
                j -= 1
                i = m
        
        return nums[i]

test_case = [ 7, 1 ]
obj = Solution()
print(obj.findMin(test_case))