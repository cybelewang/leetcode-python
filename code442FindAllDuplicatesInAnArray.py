"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
# similar problems: 645 Set Mismatch
class Solution:
    # a better solution by assigning negative sign to value in the corresponding index, we still keeps the original information and could recover the whole array
    # http://www.cnblogs.com/grandyang/p/6209746.html
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            if nums[idx] < 0:
                res.append(idx + 1)
            else:
                nums[idx] *= -1
        
        return res
            
    # my own solution, keeps swapping nums[i] with nums[nums[i]-1] until either that position nums[i]-1 is already filled or already added to result
    def findDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        twice = []
        for i, n in enumerate(nums):
            while n > 0 and n != i + 1:
                if nums[n-1] == n:
                    nums[i] = 0 # bug fixed: forgot to set nums[i] to 0 (invalid value) and leave n in nums[i], next time a value (i+1) may be switched here and triggers n to be added to res again
                    twice.append(n)
                    break
                else:
                    nums[i], nums[n-1] = nums[n-1], nums[i]
                    n = nums[i]

        return twice

nums = [4,3,2,7,8,2,3,1]
obj = Solution()
print(obj.findDuplicates(nums))