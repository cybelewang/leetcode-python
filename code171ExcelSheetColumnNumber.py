"""
171 Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in s:
            res = res * 26 + (ord(c) - ord('A') + 1)
        
        return res

obj = Solution()

test_cases = ['', 'A', 'Z', 'AA', 'AZ', 'YZ', 'ZA', 'ZZ', 'AAA', 'ZZZ']
for case in test_cases:
    print(case, end=' -> ')
    print(obj.titleToNumber(case))