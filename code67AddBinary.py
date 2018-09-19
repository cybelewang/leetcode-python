"""
67 Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""
class Solution(object):
    decode = {'1':1, '0':0}
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or len(a) == 0:
            return b

        if not b or len(b) == 0:
            return a

        build = []
        carry = 0
        for k in range(max(len(a), len(b))):
            i = len(a) - 1 - k
            j = len(b) - 1 - k
            s = carry
            if i > -1:
                s += self.decode[a[i]]
            
            if j > -1:
                s += self.decode[b[j]]

            build.append(s%2)
            carry = s//2
        
        if carry > 0:
            build.append(carry)
        
        res = ''
        for k in range(len(build)):
            res += str(build.pop())

        return res

test_cases = [('',''), ('','1'), ('0','0'), ('1','1'), ('1','0'), ('111111','1')]
obj = Solution()
for case in test_cases:
    print(case, end = ' -> ')
    print(obj.addBinary(case[0],case[1]))