"""
471 Encode String with Shortest Length

Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:

k will be a positive integer and encoded string will not be empty or have extra space.
You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
 

Example 1:

Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
 

Example 2:

Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
 

Example 3:

Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
 

Example 4:

Input: "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
 

Example 5:

Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
"""
# https://leetcode.com/problems/encode-string-with-shortest-length/discuss/95602/Short-Python
# time O(N^3)
class Solution:
    @lru_cache(None)
    def encode(self, s: str) -> str:
        n = len(s)
        i = (s + s).find(s, 1) # trick to find if s contains repeated substrings, see 459 Repeated Substring Pattern
        one = '{0}[{1}]'.format(n//i, self.encode(s[:i])) if -1 < i < n else s
        multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1, n)]
        return min([s, one] + multi, key = len)