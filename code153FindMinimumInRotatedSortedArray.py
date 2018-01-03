"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""
class Solution(object):
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
    
    # O(log(n)) solution
    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i <= j:
            m, n = (i + j)//2, j - i + 1
            if n == 1:
                return nums[i]
            else:
                if nums[i] <= nums[m] < nums[j]:
                    return nums[i]
                elif nums[i] > nums[j]:
                    if nums[m] < nums[j]:
                        j = m
                    elif nums[m] >= nums[i]:
                        i = m + 1
        
        return -1

test_case = [ 3, 4, 0, 1, 2]
obj = Solution()
print(obj.findMin(test_case))