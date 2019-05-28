"""
350 Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
from collections import defaultdict
class Solution:
    # one dictionary of the smaller array, O(m+n) time, O(m) space
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect2(nums2, nums1)

        hist1 = defaultdict(int)
        for num in nums1:
            hist1[num] += 1
        
        res = []
        for num in nums2:
            if hist1[num] > 0:
                res.append(num)
            hist1[num] -= 1
       
        return res

    # follow up: if nums1 and nums2 are sorted
    # use two pointers to compare, O(m+n) time, O(1) space
    def intersect2(self, nums1, nums2):
        i, j, res = 0, 0, []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return res

    # follow up: if nums1 and nums2 are on disk
    # If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, read chunks of array that fit into the memory, and record the intersections.
    # both nums1 and nums2 are so huge that neither fit into the memory, sort them individually (external sort), then read 2 elements from each array at a time in memory, record intersections.

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
obj = Solution()
print(obj.intersect(nums1, nums2))
print(obj.intersect2(sorted(nums1), sorted(nums2)))