"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            raise ValueError
        
        if len(digits) < 1: # Ask the result for [] + 1
            return [1]

        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s//10
        
        if carry > 0:
            digits.insert(0, carry)

        return digits

test_cases = [None, [], [0], [9], [9, 9, 8], [9, 9, 9]]

obj = Solution()
for case in test_cases:
    print(case, end = ' + 1 = ')
    print(obj.plusOne(case))

