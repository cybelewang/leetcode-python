"""
1239. Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.
Return the maximum possible length of s.
 
Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 
Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""
"""
Understand the problem correctly: 
(1) each string in arr may contain duplicate characters
(2) the eventually concatenated string must not contain duplicate characters
"""
import unittest
class Solution:
    # DFS + bit solution, TLE
    def maxLength(self, arr) -> int:
        def bit(s):
            """
            return bit-wise int which represents letters s contains
            return -1 if s contains duplicate characters
            return 0 if s is empty
            """
            mask = 0
            for c in s:
                shift = 1 << (ord(c) - ord('a'))
                if mask & (1 << shift):
                    return -1
                else:
                    mask |= (1 << shift)

            return mask

        self.ans = 0

        def dfs(arr, masks, start, mask, length):
            """
            masks: list of masks for arr
            start: start index in dfs
            mask: mask of current concatenation
            length: length of current concatenation
            """
            self.ans = max(self.ans, length)
            for i in range(start, len(arr)):
                if masks[i] >= 0 and masks[i] & mask == 0:
                    dfs(arr, masks, i+1, mask|masks[i], length + len(arr[i]))
        
        masks = list(map(bit, arr))
        dfs(arr, masks, 0, 0, 0)

        return self.ans 
            
class Test(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        self.assertEqual(obj.maxLength(["un","iq","ue"]), 4)
        self.assertEqual(obj.maxLength(["cha","r","act","ers"]), 6)
        self.assertEqual(obj.maxLength(["abcdefghijklmnopqrstuvwxyz"]), 26)
        self.assertEqual(obj.maxLength(["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]), 16)
        self.assertEqual(obj.maxLength(["zog","nvwsuikgndmfexxgjtkb","nxko"]), 4)

if __name__ == "__main__":
    unittest.main(exit=False)