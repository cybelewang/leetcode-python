"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""
from bisect import bisect_left
class Solution:
    # OJ best solution
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]    # remove last result letter because it will appear in later position
                result += c
        return result        

    # my own solution, in alphabet order, check if current letter's min position is <= remaining letters' most right positions, if yes, append this letter
    def __init__(self):
        self.alphabet = [chr(ord('a') + i) for i in range(26)]  # list stores 'a' to 'z'

    def removeDuplicateLetters2(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_pos = {}   # key:letter, value: a list of this letter's positions
        for i, c in enumerate(s):
            if c in char_pos:
                char_pos[c].append(i)
            else:
                char_pos[c] = [i]
        
        remains = len(char_pos) # number of remained characters to be added into result
        res = ''
        last_pos = -1   # last used letter's position, the next candidate letter must be at its right

        most_right_pos = [char_pos[c][-1] for c in char_pos] # each letter' most right positions        

        while remains > 0:
            min_right_pos = min(most_right_pos)   # the next possible letter's position must be <= least_right_pos
            for letter in self.alphabet:
                if letter in char_pos:
                    pos = char_pos[letter]
                    index = bisect_left(pos, last_pos + 1)
                    if pos[index] <= min_right_pos:
                        res += letter
                        most_right_pos.remove(pos[-1])
                        last_pos = pos[index]
                        char_pos.pop(letter)
                        remains -= 1
                        break
        
        return res

test_cases = ['', 'a', 'aa', 'dcba', 'bcabc', 'cbacdcbc']
obj = Solution()
for case in test_cases:
    print(case, end = ' -> ')
    print(obj.removeDuplicateLetters(case))