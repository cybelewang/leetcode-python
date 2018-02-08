"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        s, e = nums[0], nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                e = nums[i]
            else:
                if s == e:
                    res.append(str(s))
                else:
                    res.append('{0}->{1}'.format(s,e))
                s, e = nums[i], nums[i]

        # don't forget the last entry
        if s == e:
            res.append(str(s))
        else:
            res.append('{0}->{1}'.format(s,e))

        return res

test_case = [0,1,2,3,4,5,7]
obj = Solution()
print(obj.summaryRanges(test_case))