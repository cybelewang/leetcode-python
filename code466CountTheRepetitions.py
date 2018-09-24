"""
466 Count The Repetitions

Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. 
For example, “abc” can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 ≤ n1 ≤ 10^6 and 1 ≤ n2 ≤ 10^6. 
Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
"""
# similar to 418 sentence screen fitting
from collections import defaultdict
class Solution:
    # http://bookshadow.com/weblog/2016/12/04/leetcode-count-the-repetitions/
    # greedy algorithm: find the max length of s2 characters (may incomplete) while iterate all S1 characters
    # trick is how to identify the start of repetition: use greedy to identify the long strings, but hash the short string indices
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        # pre-check letter set
        if not set(s2) <= set(s1):  # check s2 issubset of s1
            return 0

        l1, l2 = len(s1), len(s2)   # unit length
        dp = defaultdict(dict)
        x1 = x2 = 0 # large indices
        while x1 < l1 * n1:
            # look for the next match
            while s1[x1 % l1] != s2[x2 % l2]:
                x1 += 1
            if x1 >= l1 * n1:
                break

            # y1, y2 corresponding small indices of s1 and s2
            y1, y2 = x1 % l1, x2 % l2

            # find the first repetitive segment
            if y2 not in dp[y1]:
                dp[y1][y2] = x1, x2 # connect short indices with long indices
            else:
                # find the repeating segment
                dx1, dx2 = dp[y1][y2]   # previous long indices
                round = (l1 * n1 - dx1) // (x1 - dx1)   # skip the repetition, 
                # goes to the last segment directly
                x1 = dx1 + round * (x1 - dx1)
                x2 = dx2 + round * (x2 - dx2)

            if x1 < l1 * n1:
                x1 += 1
                x2 += 1
        # now x2 is the length of s2 characters (including incomplete s2 characters)
        return x2 // (n2 * l2)

obj = Solution()
print(obj.getMaxRepetitions("musicforever", 10, "lovelive", 10000))
#print(obj.getMaxRepetitions("abacb", 6, "bcaa", 1))
# also see http://www.cnblogs.com/grandyang/p/6149294.html

"""
s1 small index     01234   01234   01234   01234   01234   01234
S1 large index     01234   56789   01234   56789   01234   56789
S1 --------------> abacb | abacb | abacb | abacb | abacb | abacb
S2 -------------->  b c    a a b      c    a a b      c    a a b      
S2 large index      0 1    2 3 4      5    6 7 8      9    0 1 2
s2 small index      0 1    2 3 0      1    2 3 0      1    2 3 0

repeatCount ----->    0  |   1   |   1   |   2   |   2   |   3

"""