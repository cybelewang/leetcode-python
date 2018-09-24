"""
541 Reverse String II

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. 
If there are less than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""
class Solution:
    """    
        def reverseStr_OJBest(self, s, k):
            return ''.join(s[i : i+k][::-1] + s[i+k : i+k*2] for i in range(0, len(s), k*2))
    """
    # my own solution
    # take advantage of s[start:end] which will check range automatically
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s or k < 2:
            return s

        n = len(s)
        m = n//k + 1
        a = []

        reverse, i = True, 0
        for _ in range(m):
            if reverse:
                a.append(s[i:i+k][::-1])
            else:
                a.append(s[i:i+k])

            i += k
            reverse = not reverse

        return ''.join(a)

s = 'abcd'
k = 2
print(Solution().reverseStr(s,k))