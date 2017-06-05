class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m==0 and n==0:
            return 0.0
        if m > n:
            return findMedianSortedArrays(self, num2, nums1)
        for i in range(m):
            j = (m+n+1)//2 - i
            
