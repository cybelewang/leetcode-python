"""
342 Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""
# Is 1 power of 4?
# first use power of 2 to filter
# then use special mask integer ...101010101
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return False if num <= 0 else (num & (num-1) == 0) and (num & 1431655765 != 0)

test_cases = [0, 1, 2, 4, 8, 16, 32, 4**15]

obj = Solution()
for num in test_cases:
    print(num, end = ' -> ')
    print(obj.isPowerOfFour(num))