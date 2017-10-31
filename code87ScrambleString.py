"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False

        if len(s1) < 2:
            return s1 == s2
        else:
            m, n = len(s1)//2, len(s1)
            res = False

            match1 = self.isScramble(s1[0:m], s2[0:m]) and self.isScramble(s1[m:], s2[m:])
            match2 = self.isScramble(s1[0:m], s2[m:]) and self.isScramble(s1[m:], s2[0:m])
            res = match1 or match2

            if n%2 != 0:    # odd length string cannot be split evenly
                match3 = self.isScramble(s1[0:n-m], s2[0:m]) and self.isScramble(s1[n-m:], s2[m:])
                match4 = self.isScramble(s1[0:n-m],s2[m:]) and self.isScramble(s1[n-m:],s2[0:m])
                res = res or match3 or match4

            return res

test_cases = [('',''), ('a','a'), ('ab','ba'), ('ac','ac'),('great','rgeat'),('great','rgtae'),('great','etagr')]
obj = Solution()
for case in test_cases:
    print(case[0]+' -> '+case[1]+': ', end = '')
    print(obj.isScramble(case[0],case[1]))