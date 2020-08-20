"""
Given a number and k, find the min number after removing k digits
Example: input num = 4132219, k = 3, output: 1219
follow-up: what if asking for max number?
"""
import unittest
def minNumberAfterRemovingKDigits(num, k):
    def helper(s, k):
        res = ''
        if len(s) <= k: return ''
        i, minVal = 0, '99' # change minVal to '' for follow-up
        for j in range(k+1):
            if s[j] < minVal: # we can't use <= because this will remove too many small digits, example num = 112, k = 2
                i = j
                minVal = s[j]
        if i == k:
            res = s[i:]
        else:
            res = s[i] + helper(s[i+1:], k-i)

        return res

    # can min number start from 0? I think it's OK
    s = str(num)
    if k >= len(s):
        return 0
    return int(helper(s, k))

def maxNumberAfterRemovingKDigits(num, k):
    def helper(s, k):
        res = ''
        if len(s) <= k: return ''
        i, maxVal = 0, '' # change minVal to '' for follow-up
        for j in range(k+1):
            if s[j] > maxVal: # we can't use >= because this will remove too many large digits, example num = 9923, k = 2
                i = j
                maxVal = s[j]
        if i == k:
            res = s[i:]
        else:
            res = s[i] + helper(s[i+1:], k-i)

        return res

    # can min number start from 0? I think it's OK
    s = str(num)
    if k >= len(s):
        return 0
    return int(helper(s, k))    

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(minNumberAfterRemovingKDigits(123, 1), 12)
        self.assertEqual(minNumberAfterRemovingKDigits(41129, 3), 11)
        self.assertEqual(minNumberAfterRemovingKDigits(4008, 1), 8)
        self.assertEqual(minNumberAfterRemovingKDigits(4132219, 3), 1219)
        self.assertEqual(minNumberAfterRemovingKDigits(41132219, 4), 1119)

    def test_2(self):
        self.assertEqual(maxNumberAfterRemovingKDigits(123, 1), 23)
        self.assertEqual(maxNumberAfterRemovingKDigits(9923, 2), 99)
        self.assertEqual(maxNumberAfterRemovingKDigits(41129, 3), 49)
        self.assertEqual(maxNumberAfterRemovingKDigits(4008, 1), 408)
        self.assertEqual(maxNumberAfterRemovingKDigits(4132219, 3), 4329)
        self.assertEqual(maxNumberAfterRemovingKDigits(41132219, 4), 4329)

unittest.main(exit = False)