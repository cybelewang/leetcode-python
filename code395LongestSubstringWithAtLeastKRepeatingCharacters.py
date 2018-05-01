"""
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
    # http://www.cnblogs.com/grandyang/p/5852352.html
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i, res = 0, 0
        while (len(s) - i) > res:            
            max_index = i
            mask = 0  # bit 0: >= k, bit 1: < k. bug fixed: we should not initialize mask to (1<<26) - 1 but let the inner for loop to set the bit.
            map = {}    # save the count of each character
            for j in range(i, len(s)):
                if s[j] not in map:
                    map[s[j]] = 1
                else:
                    map[s[j]] += 1
                if map[s[j]] >= k:
                    # set corresponding bit to 0
                    mask &= ~(1<<(ord(s[j]) - ord('a')))
                else:
                    # set corresponding bit to 1
                    mask |= 1<<(ord(s[j]) - ord('a'))

                if mask == 0:
                    res = max(res, j-i+1)
                    max_index = j

            i = max_index + 1

        return res

obj = Solution()
print(obj.longestSubstring("ababbc", 2))