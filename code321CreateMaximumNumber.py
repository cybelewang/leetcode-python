"""
321 Create Maximum Number

Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
"""
# OJ best solution
class BestSolution:
    def maxNumber(self, nums1, nums2, k):
        def prep(nums, k):
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a + b]

        return max(merge(prep(nums1, i), prep(nums2, k - i))
                   for i in range(k + 1)
                   if i <= len(nums1) and k - i <= len(nums2))

class Solution:
    # https://leetcode.com/problems/create-maximum-number/discuss/77291/Share-my-Python-solution-with-explanation
    # select length i from nums1, and length j from nums2, i + j = k
    # maxSingleNumber() method gets the max number from a single list with a specific length
    # mergeMax() method gets the max number from two lists 
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n, m = len(nums1), len(nums2)
        res = [0]*k
        for i in range(0, k+1):
            j = k - i
            if i > n or j > m: continue
            left = self.maxSingleNumber(nums1, i)
            right = self.maxSingleNumber(nums2, j)
            num = self.mergeMax(left, right)
            res = max(res, num)

        return res

    def maxSingleNumber(self, nums, selects):
        n = len(nums)
        res = [-1]
        if selects > n: return res
        while selects > 0:
            start = res[-1] + 1 # search start
            end = n - selects + 1 # search end
            res.append(max(range(start, end), key = nums.__getitem__))
            selects -= 1
        res = [nums[item] for item in res[1:]]
        return res

    def mergeMax(self, nums1, nums2):
        res = []
        while nums1 or nums2:
            if nums1 > nums2:
                res.append(nums1[0])
                nums1 = nums1[1:]
            else:
                res.append(nums2[0])
                nums2 = nums2[1:]
        return res

nums1 = [6, 7]
nums2 = [6, 0, 4]
obj = BestSolution()
print(obj.maxNumber(nums1, nums2, 5))