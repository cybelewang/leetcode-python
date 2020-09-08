"""
727 Minimum Window Subsequence

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.

Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
"""
from collections import defaultdict
from bisect import bisect_right
class Solution:
    # Try to build the substring with the indices map
    def minWindow(self, S: str, T: str) -> str:
        # pos[c] contains an ordered list of indices of character c in S
        pos = defaultdict(list)
        for i, c in enumerate(S):
            pos[c].append(i)
        
        # result start index and result min substring length
        rs, minLen = 0, len(S)+1
        for start in pos[T[0]]:
            end = start # end is the final substring's end index
            for c in T[1:]:
                # for each character in remaining T, we need to find its smallest position that >  current end
                i = bisect_right(pos[c], end)
                if i == len(pos[c]):
                    break
                else:
                    end = pos[c][i]
            else:
                if end - start + 1 < minLen:
                    minLen = end - start + 1
                    rs = start
        
        return S[rs:rs+minLen] if minLen < len(S) else ""