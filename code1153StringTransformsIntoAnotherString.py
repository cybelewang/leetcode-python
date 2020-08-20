"""
1153 String Transforms Into Another String

Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
 
Note:

1 <= str1.length == str2.length <= 10^4
Both str1 and str2 contain only lowercase English letters.
"""
class Solution:
    # https://leetcode.com/problems/string-transforms-into-another-string/discuss/355382/JavaC%2B%2BPython-Need-One-Unused-Character
    # one-way mapping, all same characters in s1 should map to same characters in s2
    # But they need at least one unused character to do the transformation
    # think about s1 = "abcdefghijklmnopqrstuvwxyz" and s2 = "bcdefghijklmnopqrstuvwxyza", because there is no unused character, one cannot transfom a letter to another without changing any other letter
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2: return True
        dp = {}
        for s1, s2 in zip(str1, str2):
            if dp.setdefault(s1, s2) != s2:
                return False
        
        return len(set(str2)) < 26