"""
128 Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""
# use a set (hashed in python) to search the number in O(1) time
# then start looking for consecutive numbers when the number is a start sequence (when its previous number not existing)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in num_set:
                cur = num + 1
                length = 1

                while cur in num_set:
                    cur += 1
                    length += 1
                
                res = max(res, length)
        
        return res

    # 2nd round solution on 12/17/2018
    # first put all numbers into a set
    # then for each number in nums, search for all consecutive numbers in left and right directions, if exists, remove it from set
    def longestConsecutive2(self, nums):
        num_set = set(nums)
        res = 0
        for num in nums:
            if num in num_set:
                count = 1
                num_set.discard(num)
                # search left
                i = num - 1
                while i in num_set:
                    count += 1
                    num_set.discard(i)
                    i -= 1
                # search right
                j = num + 1
                while j in num_set:
                    count += 1
                    num_set.discard(j)
                    j += 1
                # update result
                res = max(res, count)
        
        return res

obj = Solution()
test_cases = [[], [1], [1, 3], [1, 2], [100, 4, 200, 1, 3, 2]]

for case in test_cases:
    print(obj.longestConsecutive(case))
