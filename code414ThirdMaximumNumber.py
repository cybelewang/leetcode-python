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
        """
        :type nums: List[int]
        :rtype: int
        """
        f, s, t = None, None, None
        for num in set(nums):
            if f is None or num > f:
                t = s
                s = f
                f = num
            elif s is None or num > s:
                t = s
                s = num
            elif t is None or num > t:
                t = num

        return t or f

input = [2,2, 3 ,1]
obj = Solution()
print(obj.thirdMax(input))