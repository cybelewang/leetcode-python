"""
316 Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""
from bisect import bisect_left
from collections import defaultdict
class Solution:
    # OJ best solution
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        rindex = {c: i for i, c in enumerate(s)}
        A = []
        for i, c in enumerate(s):
            if c not in A:
                while A and c < A[-1] and i < rindex[A[-1]]:
                    A.pop()    # remove last letter in A because it will appear in later position
                A.append(c)
        return ''.join(A)        

    # Wrong solution. Didn't think about duplicate. See "dcba", the expected result is "dcba"?
    # my own solution, construct result in alphabet order, check if current letter's min allowed position <= all remaining letters' most right positions, if yes, append this letter
    def removeDuplicateLetters2(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabet = (chr(ord('a') + i) for i in range(26))   # 'a'-'z'
        pos = defaultdict(list)   # key:letter, value: a list of this letter's positions
        for i, c in enumerate(s):
            pos[c].append(i)
        right_pos = set([pos[c][-1] for c in pos])# each existing letter's most right positions

        total = len(pos) # number of remained characters to be added into result
        res = ''
        start = 0   # next letter's possible start position in given string s

        for _ in range(total):
            for c in alphabet:
                if c in pos:
                    index = bisect_left(pos[c], start)
                    if pos[c][index] <= min(right_pos): # the next possible letter's position must be <= least_right_pos
                        res += c
                        right_pos.remove(pos[c][-1])
                        start = pos[c][index] + 1
                        pos.pop(c)
                        break
        
        return res

test_cases = ['', 'a', 'aa', 'dcba', 'bcabc', 'cbacdcbc', 'zzddez']
obj = Solution()
for case in test_cases:
    print(case, end = ' -> ')
    print(obj.removeDuplicateLetters(case))