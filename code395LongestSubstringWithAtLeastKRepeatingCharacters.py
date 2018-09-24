"""
395 Longest Substring with At Least K Repeating Characters

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
class Solution:
    # https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87768/4-lines-Python
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
    # TLE
    # http://www.cnblogs.com/grandyang/p/5852352.html
    def longestSubstring2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i, res, n = 0, 0, len(s)
        while (n - i) > res:            
            max_index = i
            mask = 0  # bit 0: >= k, bit 1: < k. bug fixed: we should not initialize mask to (1<<26) - 1 but let the inner for loop to set the bit.
            map = [0]*26    # save the count of each character
            for j in range(i, len(s)):
                t = ord(s[j]) - ord('a')
                map[t] += 1
                if map[t] >= k:
                    # set corresponding bit to 0
                    mask &= ~(1<<t)
                else:
                    # set corresponding bit to 1
                    mask |= 1<<t

                if mask == 0:
                    res = max(res, j-i+1)
                    max_index = j

            i = max_index + 1

        return res

obj = Solution()
print(obj.longestSubstring("ababbc", 2))