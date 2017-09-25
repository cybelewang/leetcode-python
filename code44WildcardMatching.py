"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""
def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    m, n = len(s), len(p)
    match = [[False for i in range(m+1)] for j in range(n+1)] # match[i][j] is the match state of s with length i and p with length j
    match[0][0] = True # empty always matches empty


    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '?':
                match[i][j] = match[i-1][j-1]
            elif p[j-1] == '*':
                                    
            else:
                match[i][j] = match[i-1][j-1] and (s[i-1] == p[j-1])