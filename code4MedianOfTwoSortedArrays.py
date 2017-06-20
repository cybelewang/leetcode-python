class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        if n == 0:
            raise ValueError        
        iMin, iMax = 0, m
        while iMin <= iMax:
            i = (iMin + iMax)//2
            j = (m+n+1)//2 - i
            

        
            
