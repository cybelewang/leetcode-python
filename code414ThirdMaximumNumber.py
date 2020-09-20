"""
414 Third Maximum Number

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f, s, t = -2**31-1, -2**31-1, -2**31-1
        for num in set(nums):   # bug fixed: must use set to remove duplicates
            old_f, old_s = f, s
            f = max(num, f)
            s = s + (f > old_f)*(old_f - s)
            t = t + (f > old_f or s > old_s)*(old_s - t)

        return f if t == -2**31-1 else t

    def thirdMax2(self, nums):
        f, s, t = None, None, None
        for num in nums:
            if f is None or num >= f:
                if f == num: continue # bug fixed: do not update s to f if num == f                
                f, s, t = num, f, s
            elif s is None or num >= s:
                if num == s: continue # bug fixed: do not update t to s if num == s
                s, t = num, s
            elif t is None or num >= t:
                t = num
                
        return t if t is not None else f

input = [3, 2, 2]
obj = Solution()
print(obj.thirdMax2(input))