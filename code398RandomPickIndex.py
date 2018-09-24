"""
398 Random Pick Index

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
# reference http://www.cnblogs.com/grandyang/p/5875509.html
from random import randrange
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = nums        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res, count = -1, 0
        for i, num in enumerate(self.data):
            if num == target:
                count += 1
                if res == -1 or randrange(0, count) == 0:   # here res == -1 is redundant because the first time encounts a target, count == 1 and randrange(0, 1) must return 0
                    res = i
       
        return res

nums = [1,2,3,3,3]
obj = Solution(nums)
print(obj.pick(3))
print(obj.pick(3))
print(obj.pick(3))
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)