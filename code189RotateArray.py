"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II
"""
class Solution:
    # two pass. Reverse the whole array, then reverse the first k subarray, then reverse the remaining n-k subarray
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

        # reverse the whole array
        for i in range(n//2):
            nums[i], nums[n-1-i] = nums[n-1-i], nums[i]
        
        # reverse the first k subarray
        for i in range(k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
        
        # reverse the remaining n-k subarray
        for i in range((n-k)//2):
            nums[k + i], nums[n-1-i] = nums[n-1-i], nums[k + i]
    
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or k <= 0:
            return

        s, n = 0, len(nums)

        while n > 1 and k % n > 0: # bug fixed: if we don't have k%n > 0, it will be in dead loop for k == n
            k = k % n
            if k > n//2: # right part (length k) is longer, so we swap the left part (length n-k) with the most right (n-k) subarray
                for i in range(n-k):
                    nums[s + i], nums[s + i + k] = nums[s + i + k], nums[s + i]
                temp = n
                n = k # only need to process the most left k subarray because the most right n-k subarray are in good position
                k = 2 * k - temp # we still need to rotate these steps, using a graph to analyze it
            else: # left part (length n-k) is longer, so we swap the right part (length k) with the most left (k) subarray
                for i in range(k):
                    nums[s + i], nums[s + i + n - k] = nums[s + i + n - k], nums[s + i]
                s += k # after swapping, we need to advance the start index
                n = n - k # we still need to process the remaining (n-k) part

    # use an extra memory to save the shifted out subarray, Space O(n), time O(n)
    def rotate3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or k <= 0:
            return

        n = len(nums)
        k = k % n

        remain = nums[n-k:] # save the shifted out subarray
        for i in range(n-k): # shift the left part to right
            nums[n-1-i] = nums[n-k-1-i]
        
        for i in range(k): # arrapy the shifted out subarray to left
            nums[i] = remain[i]

test_case = [1, 2, 3, 4, 5, 6, 7]
obj = Solution()
obj.rotate2(test_case, 3)
print(test_case)