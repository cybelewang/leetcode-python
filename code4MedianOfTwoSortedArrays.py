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
            # this guarantees m <= n
            # therefore, when i > 0, j < n, see onenote
            # when i < m, j > 0, see onenote
            m, n, nums1, nums2 = n, m, nums2, nums1
        if n == 0:
            raise ValueError        
        iMin, iMax = 0, m
        while iMin <= iMax:
            i = (iMin + iMax)//2
            j = (m+n+1)//2 - i
            if i>0 and nums1[i-1] > nums2[j]:   # i > 0 guarantees j < n
                iMax = i - 1
            elif i < m and nums1[i] < nums2[j-1]:   # we cannot use j > 0 as the condition because j > 0 cannot guarantee i < m, but i < m can guarantee j > 0
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
    # 2nd round solution on 6/15/2019, easier to understand
    # solution 1 from https://www.cnblogs.com/grandyang/p/4465932.html
    def findMedianSortedArrays2(self, nums1, nums2):
        INT_MAX = 2**31
        def findKth(A, i, B, j, k):
            m, n = len(A), len(B)
            if i >= m:  return B[j+k-1]
            if j >= n:  return A[i+k-1]
            if k == 1:  return min(A[i], B[j])
            midVal1 = INT_MAX if i + k//2 - 1 >= m else A[i+k//2-1]
            midVal2 = INT_MAX if j + k//2 - 1 >= n else B[j+k//2-1]
            if midVal1 < midVal2:
                return findKth(A, i+k//2, B, j, k-k//2)
            else:
                return findKth(A, i, B, j+k//2, k-k//2)
        
        m, n = len(nums1), len(nums2)
        left, right = (m+n+1)//2, (m+n+2)//2
        return (findKth(nums1, 0, nums2, 0, left) + findKth(nums1, 0, nums2, 0, right))/2.0

            
nums1, nums2 = [1, 3], [2]
print(Solution().findMedianSortedArrays2(nums1, nums2))