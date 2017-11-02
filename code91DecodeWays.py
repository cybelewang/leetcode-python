"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

"""
# dynamic programming
# First use an array ways[]
# Then reduce to extra two variables pre1, pre2
class Solution:
    def __init__(self):
        self.decode = {}
        for i in range(1, 27):  # bug fixed: change 26 to 27
            self.decode[str(i)] = True
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        pre2 = 1 if s[0] in self.decode else 0

        if len(s) < 2: # bug fixed here: forgot to handle length == 1
            return pre2

        pre1 = 0
        if s[1] in self.decode:
            pre1 = pre2
        if s[0:2] in self.decode:
            pre1 += 1

        cur = pre1
        for i in range(2, len(s)):
            cur = pre1 if s[i] in self.decode else 0
            
            if s[i-1:i+1] in self.decode:
                cur += pre2
            
            pre2 = pre1
            pre1 = cur
        
        return cur

test_cases = ['', '0', '01', '1', '10', '12', '123', '1203', '1020', '1111']
obj = Solution()
for case in test_cases:
    print(case, end = ' -> ')
    print(obj.numDecodings(case))