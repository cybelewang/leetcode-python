"""
686 Repeated String Match

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.

"""
class Solution:
    # my own solution
    # first make A's length >= B's length
    # then check if B is in A, if not try to append one more A, and check again
    # try example A = 'abc', B = 'cabcab'
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        m, n = len(A), len(B)
        res = n//m if n%m == 0 else n//m + 1
        s = A*res
        if s.count(B) > 0:
            return res

        if (s + A).count(B) > 0:
            return res + 1

        return -1

A, B = 'abcd', 'dabcdabcda'
print(Solution().repeatedStringMatch(A, B))
