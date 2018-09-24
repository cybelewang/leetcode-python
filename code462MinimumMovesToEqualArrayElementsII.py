"""
462 Minimum Moves to Equal Array Elements II

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, 
where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""
class Solution:
    # similar to 296 Best Meeting Point
    # http://www.cnblogs.com/grandyang/p/6089060.html
    # consider an array with only two elements, the minimum moves is the absolute difference between the two numbers
    # so we can sort the number first, then for each symmetric paired numbers, the difference is the minimum move
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)-1
        nums.sort()
        res = 0
        while (i < j):
            res += nums[j] - nums[i]
            i += 1
            j -= 1

        return res

    # wrong solution
    # mathmatically, the target number or base is the average of all numbers
    def minMoves2_wrong(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        sum_ = sum(nums)

        if sum_ < 0:
            base = -int(-sum_/len(nums) + 0.5)
        else:
            base = int(sum_/len(nums) + 0.5)
        
        res = 0
        for num in nums:
            res += abs(num - base)

        return res

nums = [1, 0, 0, 8, 6]
print(Solution().minMoves2(nums))
        