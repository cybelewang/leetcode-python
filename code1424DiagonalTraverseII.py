"""
1424 Diagonal Traverse II

Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.

Example 1:

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
Example 2:

Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
Example 3:

Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
Output: [1,4,2,5,3,8,6,9,7,10,11]
Example 4:

Input: nums = [[1,2,3,4,5,6]]
Output: [1,2,3,4,5,6]

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= nums[i][j] <= 10^9
There at most 10^5 elements in nums.
"""
class Solution:
    # Best solution, time O(n), space O(n), where n is the total number of elements
    # https://leetcode.com/problems/diagonal-traverse-ii/discuss/597794/Python-One-pass
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i, r in enumerate(nums):
            for j, a in enumerate(r):
                if i + j == len(res):
                    res.append([])
                res[i + j].append(a)
        return [a for r in res for a in reversed(r)]    
    # AC solution, time O(n*logn) where n is the total number of elements
    def findDiagonalOrder2(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                ans.append((r+c, c, nums[r][c]))
        ans.sort()
        return [v for _, _, v in ans]
    # TLE solution, time O(M*N) where N is the max column width
    def findDiagonalOrder3(self, nums: List[List[int]]) -> List[int]:
        m, n = len(nums), 0
        for a in nums: n = max(n, len(a))
        res = []
        for k in range(m + n - 1):
            for r in range(min(k, m - 1), max(k - n, -1), -1):
                c = k - r
                if c < len(nums[r]):
                    res.append(nums[r][c])
        return res