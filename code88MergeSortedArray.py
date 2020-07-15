"""
88 Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m < 0 or n < 1:  # bug fixed here: should not use m < 1, consider m = 0 and n = 1
            return

        i, j = m - 1, n - 1   # index for nums1, nums2, and the new array
        for k in range(m + n - 1, -1, -1):
            if i > -1 and (j < 0 or (j > -1 and nums1[i] >= nums2[j])):
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
    
    # 2nd round visit on 7/11/2020
    # Bugs fixed. The mistake was using j < 0 as indicator of completition and if j > -1, we will continuously decrease i or j. Think about test case nums1=[2,0] and nums2=[1]. i actually goes to -1.
    def merge2(self, nums1, m, nums2, n):
        if n < 1: return
        i, j = m-1, n-1
        INT_MIN = -2**31
        for k in range(m+n-1, -1, -1):
            a = nums1[i] if i > -1 else INT_MIN
            b = nums2[j] if j > -1 else INT_MIN
            if a > b:
                nums1[k] = a
                i -= 1
            else:
                nums1[k] = b
                j -= 1   
        

nums1 = [5,7,8,9,0,2,3]
nums2 = [11,12,15]

obj = Solution()
obj.merge(nums1, 4, nums2, 3)
print(nums1)
        
