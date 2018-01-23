"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""
# use two maps to track mapping because no two characters map to the same character
# note 'bao' and 'foo' should be false because 'a':'o' and 'o':'o'. It's tricky to understand "a character may map to itself", so if s[i]==t[i], it's already mapping, we cannot ignore it. see failed submission in OJ.
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '':
            return True
        
        s_t, t_s = {}, {}
        for i in range(len(s)):            
            if t[i] in t_s and s[i] != t_s[t[i]]:
                return False
            elif s[i] in s_t and t[i] != s_t[s[i]]:
                return False
            else:
                t_s[t[i]] = s[i]
                s_t[s[i]] = t[i]
        
        return True

test_cases = [('egg', 'add'), ('foo', 'bar'), ('foo', 'bao'), ('paper', 'title'), ('pae', 'too'), ('ab', 'aa')]
obj = Solution()
for case in test_cases:
    print(obj.isIsomorphic(case[0], case[1]))