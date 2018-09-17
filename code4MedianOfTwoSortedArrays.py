"""
4 Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
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
            if i>0 and nums1[i-1] > nums2[j]:
                iMax = i - 1
            elif i<m and nums1[i] < nums2[j-1]:
                iMin = i + 1 # why i + 1?
            else:
                # perfect i
                if i==0:
                    max_left = nums2[j-1]
                elif j==0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])

                if (m+n)%2==1:
                   return max_left

                if i==m:
                    min_right = nums2[j]
                elif j==n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i],nums2[j])
                
                return (max_left + min_right)/2.0
                        
            
