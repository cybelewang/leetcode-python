"""
163 Missing Ranges

Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
Example:
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""
class Solution:
    def findMissingRanges(self, nums, lower, upper):
        a, res = lower, []
        for num in nums:
            if num > upper:
                break
            if num >= lower:
                b = num - 1
                if a == b:
                    res.append(str(a))
                elif a < b:
                    res.append(str(a)+'->'+str(b))
                a = num + 1
        # make sure upper is processed
        b = upper
        if a == b:
            res.append(str(a))
        elif a < b:
            res.append(str(a)+'->'+str(b))
        return res
