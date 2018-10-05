"""
791 Custom Sort String

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 

Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
"""
from collections import Counter
class Solution:
    # my own solution with bug fixed
    # count letters in T, for each letter in S, concatenate corresponding number of letters in result, finally concatenate the remaining letters in T
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        count = Counter(T)
        res = []
        for c in S:
            res.append(c*count[c])
            count[c] = 0    # bug fixed: previously used count.pop(c) and caused key error for test case S = "cbafg" and T = "abcd"
        
        # bug fixed: forgot the letters not in S
        for c in count:
            res.append(c*count[c])

        return ''.join(res)

S="cbafg"
T="abcd"
print(Solution().customSortString(S, T))
