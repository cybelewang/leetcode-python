"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, 
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""
class Solution:
    # my own solution using regular expression to find all occurrences of '01' and '10' first
    # then for each '01' or '10', expand them along two directions and check if they are symmetric
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #start = [m.start() for m in re.finditer('01|10', s)]    # re.finditer() only returns non-overlapping occurrences
        res = 0
        for k in range(len(s)-1):
            if s[k:k+2] in ('10', '01'):
                res += 1
                i, j = k, k+1
                while i > 0 and j < len(s)-1 and s[i-1] == s[i] and s[j+1] == s[j]:
                    res += 1
                    i -= 1
                    j += 1
                
        return res

s = "00110011"
print(Solution().countBinarySubstrings(s))

"""
https://leetcode.com/problems/count-binary-substrings/discuss/108600/Java-O(n)-Time-O(1)-Space
public int countBinarySubstrings(String s) {
    int prevRunLength = 0, curRunLength = 1, res = 0;
    for (int i=1;i<s.length();i++) {
        if (s.charAt(i) == s.charAt(i-1)) curRunLength++;
        else {
            prevRunLength = curRunLength;
            curRunLength = 1;
        }
        if (prevRunLength >= curRunLength) res++;
    }
    return res;
}
"""
