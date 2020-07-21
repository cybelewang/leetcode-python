"""
424 Longest Repeating Character Replacement

Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. 
Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 10^4.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
# similar to: longest substring with at most k distinct characters
class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i, j, count, base = 0, 0, [0]*26, ord('A')
        while j < len(s):
            count[ord(s[j]) - base] += 1
            j += 1
            if j - i - max(count) > k: # (j-i) is the current window size, or the current result to return until this loop step
                # we need to maintain the window size by rolling s[i] out (j increases by 1, so window size j - i doesn't change)
                count[ord(s[i]) - base] -= 1
                i += 1
            # if j - i <= max(count) + k, we don't need to roll s[i] out
        # s[i:j+1] may not be always valid, see s="AAABB" and k=1, when i=1, j =4, but j-i keeps the largest valid window size
        return j - i

s = "ABCABBC"
obj = Solution()
print(obj.characterReplacement(s, 2)) # "CA" can be replaced by "BB", thus result is 5
s = "AAABB"
print(obj.characterReplacement(s, 1))
"""
https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91278/7-lines-C++
Based on the Python solution by @dalwise. Use a sliding window s[i:j], always add the new character, and remove the first window character if the extension isn't ok. So in each step, either extend the window by one or move it by one.

int characterReplacement(string s, int k) {
    int i = 0, j = 0, ctr[91] = {};
    while (j < s.size()) {
        ctr[s[j++]]++;
        if (j-i - *max_element(ctr+65, ctr+91) > k)
            ctr[s[i++]]--;
    }
    return j - i;
}
"""        