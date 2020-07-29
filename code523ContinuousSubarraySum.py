"""
523 Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""
# similar problems: 560
class Solution:
    # https://leetcode.com/problems/continuous-subarray-sum/discuss/99499/Java-O(n)-time-O(k)-space
    # convert from sum = n*k to sum % k = 0
    # we just iterate all number, and calculate running sum % k, and put running sum % k into a map, 
    # if we find another running sum % k in later number, we find sum = n * k
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum_, mem = 0, {0:-1}# bug fixed: forgot to add {0:-1}. Think about [0, 0] and k = 0
        
        for j, num in enumerate(nums):
            sum_ += num
            if k != 0:  # bug fixed: forgot to handle k = 0
                sum_ %= k
            if sum_ in mem:
                i = mem[sum_]
                if j - i > 1:
                    return True
            else:
                mem[sum_] = j
        
        return False

    # 7/25/2020 
    # O(n) space, no need of accumulation list
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        k = abs(k)
        sums = 0
        mem = {0:-1}
        for i, num in enumerate(nums):
            sums += num
            if k == 0:
                if sums in mem and i - mem[sums] >= 2:
                    return True
                mem.setdefault(sums, i)
            if k > 0:
                if sums%k in mem and i - mem[sums%k] >= 2:
                    return True
                mem.setdefault(sums%k, i)
        return False            

nums = [0,0]
k=0
print(Solution().checkSubarraySum(nums, k))