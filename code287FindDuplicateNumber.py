"""
287 Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
class Solution:
    # loop detection used in linked list cycle detection
    # see https://segmentfault.com/a/1190000003817671
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        find = 0
        while find != slow:
            slow = nums[slow]
            find = nums[find]
        
        return find

    # binary search solution, O(NlogN)
    def findDuplicate2(self, nums):
        n = len(nums)
        left, right = 1, n-1
        while left < right:
            mid = (left + right)//2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        
        return right

    # bit manipulation
    def findDuplicate3(self, nums):
        res, n = 0, len(nums)
        for i in range(32):
            bit, cnt1, cnt2 = 1 << i, 0, 0
            for k in range(n):  # here n is different from the description's n
                if k & bit: cnt1 += 1
                if nums[k] & bit: cnt2 += 1
            
            if cnt2 > cnt1:
                res += bit
        
        return res

test_case = [1, 3, 4, 2, 1]
test_case = [1,1,2,3,4,5,6]
obj = Solution()
print(obj.findDuplicate3(test_case))