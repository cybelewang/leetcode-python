"""
80 Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i, count = 1, 1 # i: the index to be copied to.    count: the count of current repeated number
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                count += 1
            else:
                count = 1
                
            if count < 3:
                nums[i] = nums[j]
                i += 1

        return i

# 2nd round solution on 9/19/2018
class Solution2:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n < 3:   return n
        last, count, insert = nums[0], 1, 1
        for i in range(1, n):
            if nums[i] == last:
                if count < 2:
                    count += 1
                    nums[insert] = nums[i]
                    insert += 1
            else:
                nums[insert] = nums[i]
                insert += 1
                last, count = nums[i], 1

        return insert

test_cases = [[],[1],[1,1],[1,1,1],[1,1,1,2,2,3],[1,1,1,2,2,2,2,2],[1,1,2,2,3,3,3,3]]
obj = Solution()
for case in test_cases:
    print(case, end = ' -> ')
    print(obj.removeDuplicates(case))
        