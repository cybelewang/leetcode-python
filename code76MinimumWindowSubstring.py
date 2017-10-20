"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return 0

        res = ''

        # Build the required count map
        required, requires = {}, len(t)
        for c in t:
            if c in required:
                required[c] = required[c] + 1
            else:
                required[c] = 1
        
        # Find the left start index
        i = 0
        for (i, c) in enumerate(s):
            if c in required:
                break

        for j in range(i, len(s)):
            c = s[j]
            if c in required:
                required[c] = required[c] - 1   # decrease the required count of c by 1
                if required[c] >= 0:    # required[c] may < 0 because there are more than required "c" in s[i:j+1]
                    requires -= 1
                if requires == 0:
                    # Update the res
                    if not res or (j - i + 1) < len(res):
                        res = s[i:j+1]
                    # Now keep increasing left index until requires > 0
                    i += 1
                    while requires == 0 and i < len(s):
                        if s[i] in required:
                            required[s[i]] = required[s[i]] + 1
                            if required[s[i]] > 0:
                                requires += 1
                        i += 1
                    # Now keep increasing left index until next required character is hit
                    while i < len(s) and s[i] not in required:
                        i += 1
        
        return res

test_cases = [("ADOBECODEBANC","ABC")]
obj = Solution()
for case in test_cases:
    print(obj.minWindow(case[0],case[1]))

                
                    
