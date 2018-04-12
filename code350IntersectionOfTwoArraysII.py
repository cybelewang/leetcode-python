"""
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
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hist1, hist2 = {}, {}
        for num in nums1:
            if num not in hist1:
                hist1[num] = 0
            hist1[num] += 1
        
        for num in nums2:
            if num not in hist2:
                hist2[num] = 0
            hist2[num] += 1

        res = []
        for num in set(hist1.keys()) & set(hist2.keys()):
            res.extend([num]*min(hist1[num], hist2[num]))
        
        return res

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
obj = Solution()
print(obj.intersect(nums1, nums2))