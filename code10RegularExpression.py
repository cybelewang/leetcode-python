"""
10 Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

"""
# similar problems: 44 Wildcard Matching
import unittest
def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    m, n = len(s), len(p)
    match = [[False for y in range(n+1)] for x in range(m+1)] # match[i][j] means if s[0:i] matches p[0:j]
    
    match[0][0] = True; # empty always matches empty
    for j in range(2, n+1):
        if p[j-1] == "*":
            match[0][j] = match[0][j-2]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == ".":
                match[i][j] = match[i-1][j-1]
            elif p[j-1] == '*':
                if j >= 2:  
                    match0 = match[i][j-2]                  
                    if p[j-2] == ".":
                        match1 = match[i-1][j-2]
                        matchN = match[i-1][j]
                    else:
                        match1 = match[i-1][j-2] and (s[i-1] == p[j-2])
                        matchN = match[i-1][j] and (s[i-1] == p[j-2])
                    match[i][j] = match0 or match1 or matchN
            else:
                # normal character
                match[i][j] = match[i-1][j-1] and (s[i-1] == p[j-1])

    return match[m][n] 

def isMatch2(s, p):
    m, n = len(s), len(p)
    match = [[False]*(1+n) for _ in range(1+m)]
    match[0][0] = True
    
    for j in range(1, n+1):
        if p[j-1] == '*':
            match[0][j] = match[0][j-2]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '.':
                match[i][j] = match[i-1][j-1]
            elif p[j-1] == '*':
                match0 = match[i][j-2]
                if p[j-2] == '.':
                    match1 = match[i-1][j-2]
                    matchN = match[i-1][j]
                else:
                    match1 = match[i-1][j-2] and (s[i-1] == p[j-2])
                    matchN = match[i-1][j] and (s[i-1] == p[j-2])
                match[i][j] = match0 or match1 or matchN
            else:
                match[i][j] = match[i-1][j-1] and (s[i-1] == p[j-1])
    
    return match[m][n] 

class Test(unittest.TestCase):
    def test1(self):            
        test_case = [("","", True),("","a*", True),("",".*", True),("",".*.*", True),("a","", False),("abcd","abc*d", True),("abcc","abc*", True),("ab","abc*", True),("abc",".*cd", False),("aa","a", False),("aaa","aa", False),("aa",".*", True),("ab",".*", True),("aab","c*a*b", True)]
        for (s, p, expected) in test_case:
            if isMatch(s, p) != expected:
                print("s: {}, p: {}, expected: {}".format(s, p, expected))
            self.assertEqual(isMatch(s, p), expected)

    def test2(self):            
        test_case = [("","", True),("","a*", True),("",".*", True),("",".*.*", True),("a","", False),("abcd","abc*d", True),("abcc","abc*", True),("ab","abc*", True),("abc",".*cd", False),("aa","a", False),("aaa","aa", False),("aa",".*", True),("ab",".*", True),("aab","c*a*b", True)]
        for (s, p, expected) in test_case:
            if isMatch2(s, p) != expected:
                print("s: {}, p: {}, expected: {}".format(s, p, expected))
            self.assertEqual(isMatch2(s, p), expected)

unittest.main(exit = False)