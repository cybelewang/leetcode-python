"""
532 K-diff Pairs in an Array

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""
import unittest
from collections import Counter
class Solution:
    # my own solution: (fixed a bug: there is a test case of k = -1)
    # k > 0, we add k to nums, and check the number of intersected elements with original nums
    # k = 0, we check the number of elements whose count > 1
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        if k > 0:
            required = [i + k for i in nums]
            res = len(set(nums) & set(required))
        elif k == 0:
            count = Counter(nums)
            res = len([x for x in count if count[x] > 1])
        
        return res
    
    # 2nd round solution on 7/1/2019
    # wrong because the problem requires "unique" diff-k pairs
    def findPairs2(self, nums, k):
        if not nums or k < 0:
            return 0
        
        count, res = {}, 0
        for num in nums:
            res += count.get(num + k, 0)
            if k > 0:
                res += count.get(num - k, 0)
            count[num] = count.get(num, 0) + 1
        
        return res

class Test(unittest.TestCase):
    def test_empty(self):
        obj = Solution()
        self.assertEqual(obj.findPairs([], 0), 0)
        self.assertEqual(obj.findPairs([], -1), 0)
        self.assertEqual(obj.findPairs([], -1), 0)
        self.assertEqual(obj.findPairs([1, 2], -1), 0)

    def test_small(self):
        obj = Solution()
        self.assertEqual(obj.findPairs([1, 2, 3, 4, 5], 1), 4)
        self.assertEqual(obj.findPairs([1,2,3,4,5], 2), 3)
        self.assertEqual(obj.findPairs([3,1,4,1,5],2), 2)

    def test_k0(self):
        obj = Solution()
        self.assertEqual(obj.findPairs([1, 3, 1, 2, 5], 0), 1)

# run unit test
if __name__ == '__main__':
    unittest.main(exit=False)
