"""
87 Scramble String

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
# to be clear: the binary tree may not equally divide the parent string, 'great' may be divided to 'g|reat'
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
            f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False

# 2nd round solution on 9/13/2018
class Solution2:
    def isScramble(self, s1, s2):
        m, n = len(s1), len(s2)
        if m != n or sorted(s1) != sorted(s2): return False
        if n < 4 or s1 == s2: return True
        f = self.isScramble
        for i in range(1, n):
            if (f(s1[:i], s2[:i]) and f(s1[i:], s2[i:])) or (f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i])):
                return True
        
        return False

test_cases = [('',''), ('a','a'), ('ab','ba'), ('abc','bac'), ('ac','ac'),('great','rgeat'),('great','rgtae'),('great','etagr')]
obj = Solution2()
for case in test_cases:
    print(case[0]+' -> '+case[1]+': ', end = '')
    print(obj.isScramble(case[0],case[1]))