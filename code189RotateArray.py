"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II
"""
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or k <= 0:
            return

        n = len(nums)
        k = k % n

        remain = nums[n-k:]
        for i in range(n-k):
            nums[n-1-i] = nums[n-k-1-i]
        
        for i in range(k):
            nums[i] = remain[i]

test_case = [1, 2, 3, 4, 5, 6, 7]
obj = Solution()
obj.rotate(test_case, 3)
print(test_case)