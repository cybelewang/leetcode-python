"""
306 Additive Number

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
"""
class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def addStr(num1, num2):
            """
            Add two strings (contain digits) and return the result as a string
            :type num1: str
            :type num2: str
            :rtype: str
            """
            res, carry = [], 0
            for i in range(max(len(num1), len(num2))):
                n1 = 0 if i >= len(num1) else ord(num1[-i-1]) - ord('0')
                n2 = 0 if i >= len(num2) else ord(num2[-i-1]) - ord('0')
                value = n1 + n2 + carry
                res.append(str(value%10))
                carry = value//10

            if carry != 0:
                res.append(str(carry))

            return ''.join(res[::-1])

        def check(num, num1, num2, k):
            """
            Check if num1 plus num2 is in num[k:]
            :type num1: str
            :type num2: str
            :rtype: bool
            """
            if k == len(num):
                return True

            num3 = addStr(num1, num2)            
            l = k + len(num3)
            if l <= len(num) and num[k:l] == num3:
                return check(num, num2, num3, l)
            else:
                return False

        # main function body
        if len(num) < 3:
            return False

        for j in range(1, len(num)-1):  # pitfall here: be careful of the range limit
            if num[0] == '0' and j > 1:
                break
            num1 = num[0:j]
            for k in range(j+1, len(num)):
                if num[j] == '0' and k > j+1:
                    break
                num2 = num[j:k]
                if check(num, num1, num2, k):
                    return True
        
        return False

test_cases = ['','123','1023','112358','00000', '199100199']
obj = Solution()
for case in test_cases:
    print(case, end='->')
    print(obj.isAdditiveNumber(case))

