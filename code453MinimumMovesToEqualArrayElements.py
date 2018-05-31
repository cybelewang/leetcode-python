"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""
class Solution:
    # my own solution!
    # the min of nums will always be added 1
    # assume the final equal value is M, then M - min is what we want, and we assume x = M - min
    # The sum of the final equal list is n*M, where n is the length of array
    # We know that n*M = sum(nums) + (n-1)*x = n(x+min), so x = sum(nums) - n*min
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums)*min(nums)

nums = [1, 2, 3]
obj = Solution()
print(obj.minMoves(nums))