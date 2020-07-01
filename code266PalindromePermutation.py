"""
266. Palindrome Permutation

Given a string, determine if a permutation of the string could form a palindrome.
Example 1:
Input: "code"
Output: false
Example 2:
Input: "aab"
Output: true
Example 3:
Input: "carerac"
Output: true
"""
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        m = set()
        for c in s:
            if c in m:
                m.remove(c)
            else:
                m.add(c)
        
        return len(m) < 2