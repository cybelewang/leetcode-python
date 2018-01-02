"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
# There are three possibilities to get a max product from subarray: current num, previous positive * current num, previous negative * current num
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        p1, p2, res = 1, 1, nums[0]
        for num in nums:
            temp = p1
            p1 = max(p1*num, p2*num, num)
            p2 = min(temp*num, p2*num, num)
            res = max(res, p1)
        
        return res

test_cases = [[2, 3, -2, 4], [2,-5,-2,-4,3]]
obj = Solution()

for case in test_cases:
    print(obj.maxProduct(case))
