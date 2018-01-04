"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.
"""
class Solution:
    # OJ best solution, single side comparison, good for find the 1st peak
    def findPeakElement(self, nums):
        peak = nums[0]
#        l = len(nums)
#        if l <= 1:
#            return 0
        for i in range(len(nums)):
            if nums[i] < peak:
                return i - 1
            elif nums[i] >= peak:
                peak = nums[i]
        return i
    
    # my improved solution, good for find all peaks
    def findPeakElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ascend = True
        for i in range(len(nums)-1):            
            if ascend and nums[i] > nums[i+1]:
                return i
            ascend = nums[i] < nums[i+1]

        return len(nums) - 1 if ascend else -1 

    # two sides comparison
    def findPeakElement3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(-2**31-1)
        for i in range(len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        # nums.pop()    # restore nums

        return -1

obj = Solution()
test_cases = [[], [1], [1, 2], [1, 2, 3, 1]]
for case in test_cases:
    print(case, end=' -> ')
    print(obj.findPeakElement2(case))