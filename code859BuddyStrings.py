"""
859 Buddy Strings

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""
class Solution:
    # ask about corner case "" and "a"
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        m, n = len(A), len(B)
        if m != n or m < 2:
            return False
        
        diff, pair = 0, []
        for i in range(m):
            if A[i] != B[i]:
                diff += 1
                pair.append((A[i], B[i]))
            if diff > 2:
                return False
        if diff == 0:
            return len(set(A)) < len(A)
        elif diff == 1:
            return False
        else:
            return pair[0] == pair[1][::-1]

test_cases = [("", ""), ("ab", "ba"), ("aa", "aa"), ("abc", "abb"), ("abc", "abc")]
for A, B in test_cases:
    print(Solution().buddyStrings(A, B))
        
