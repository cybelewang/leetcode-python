"""

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence a_i, a_j, a_k such that i < j < k and a_i < a_k < a_j. 
Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""
class Solution:
    # http://www.cnblogs.com/grandyang/p/6081984.html
    # https://leetcode.com/problems/132-pattern/discuss/94071/Single-pass-C++-O(n)-space-and-time-solution-(8-lines)-with-detailed-explanation.
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        third, stack = -2**31, []   # third is a_k, or '2' in '132'

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < third:
                return True
            else:
                while stack and nums[i] > stack[-1]:# stack elements are in descending order
                    third = stack.pop()# this assures third will be the largest number that < nums[i]
                stack.append(nums[i])

        return False
    # wrong solution because the problem requires ai < ak < aj, and the below solution only assures ai < aj, aj > ak, may consider using Java's treeset or C++'s lower_bound when searching from right to left
    # two pass, first pass from left to right, mark each number if there's a smaller number on its left
    # second pass from right to left, check each number if there's a smaller number on its right
    def find132pattern2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False

        left_rise = [False]
        minVal = nums[0]

        for i in range(1, n):
            if nums[i] > minVal:
                left_rise.append(True)
            else:
                minVal = nums[i]
                left_rise.append(False)

        minVal = nums[-1]
        for i in range(n-1, 0, -1):
            if nums[i] > minVal:
                if left_rise[i]: return True
            else:
                minVal = nums[i]

        return False

nums = [1, 5, 3, 4]
obj = Solution()
print(obj.find132pattern(nums))
