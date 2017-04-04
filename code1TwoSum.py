class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        records = {}
        for (idx, num) in enumerate(nums):
            if (target - num) in records:
                return [records[target - num], idx]
            else:
                records[num] = idx
        return None