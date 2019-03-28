"""
984 String Without AAA or BBB

Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.

Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: A = 4, B = 1
Output: "aabaa"

Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B.
"""
# tag: greedy
class Solution:
    # my own solution
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A < B:
            res = self.strWithout3a3b(B, A)
            res = res.replace('a', 'c')
            res = res.replace('b', 'a')
            res = res.replace('c', 'b')
            return res
        
        res = ""
        # append "aab" to consume A twice faster than B
        while A > B > 0:
            res += "aab"
            A -= 2
            B -= 1
        
        # now either B has all been consumed or A <= B, append "a" then "b"
        while A > 0 or B > 0:
            if A > 0:
                res += 'a'
                A -= 1
            if B > 0:
                res += 'b'
                B -= 1
        
        return res

A, B = 12, 20
print(Solution().strWithout3a3b(A, B))