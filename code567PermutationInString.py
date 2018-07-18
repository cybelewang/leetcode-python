"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
# similar problems: 438

class Solution:
    # my own solution, use a 32-bit integer to represent each letter's count match s1
    # use a fixed-size window (length of s1) to scan s2, and update mask each time and check if mask is 0 (permutation found)
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def update_mask(count1, count2, idx, mask):
            if count2[idx] == count1[idx]:
                mask = mask & (~(1 << idx))
            else:
                mask = mask | (1 << idx)

            return mask

        if len(s1) > len(s2):
            return False

        count1, count2 = [0]*26, [0]*26
        mask = 0

        for letter in s1:
            idx = ord(letter) - ord('a')
            count1[idx] += 1
            mask = mask | (1 << idx)

        for i, c in enumerate(s2):
            idx = ord(c) - ord('a')
            count2[idx] += 1
            mask = update_mask(count1, count2, idx, mask)

            if i >= len(s1) - 1:    # bug fixed
                if mask == 0:
                    return True
                idx = ord(s2[i-len(s1)]) - ord('a')
                count2[idx] -= 1
                mask = update_mask(count1, count2, idx, mask)

        return False

s1, s2 = 'ab', 'eidbaooo'
print(Solution().checkInclusion(s1, s2))