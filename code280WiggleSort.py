"""
280 Wiggle Sort
 
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
"""
class Solution:
    # https://www.cnblogs.com/grandyang/p/5177285.html
    # O(N) solution
    # if i is odd, then nums[i-1] <= nums[i]
    # if i is even, then nums[i-1] >= nums[i]
    # if above is not true, then swap nums[i-1] and nums[i]
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if (i&1 and nums[i] < nums[i-1]) or (i&1==0 and nums[i] > nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]

    # Quick select + list assignment
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2: return
        def partition(nums, s, e):
            i = s
            for j in range(s, e):
                if nums[j] < nums[e]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[e] = nums[e], nums[i]
            return i    

        left, right = 0, n - 1
        while left < right:
            i = partition(nums, left, right)
            if i + 1 == (n + 1) // 2: break
            elif i + 1 < (n + 1) // 2:
                left = i + 1
            else:
                right = i - 1
        
        nums[0:n:2], nums[1:n:2] = nums[:(n+1)//2], nums[(n+1)//2:]

    # O(NlogN) solution
    def wiggleSort2(self, nums):
        """
        :type nums: list[int]
        :rtype: none
        """
        nums.sort()
        for i in range(2, len(nums), 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]
        
nums = [1, 2, 3, 6, 4, 5]
Solution().wiggleSort(nums)
print(nums)        