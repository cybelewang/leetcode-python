"""
926 Flip String to Monotone Increasing

A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.

Note:

1 <= S.length <= 20000
S only consists of '0' and '1' characters.
"""
class Solution:
    # my own solution by partitioning S to two parts S[:i] and S[i+1:]
    # we need to change all '1's in left part to '0', so we need to count '1' in S[:i]
    # we also need to change all '0's in right part to '1', so we need to count '0' in S[i+1:]
    # iterate all different partitioning positions and get the answer
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        ones = [0]*(n+1)    # ones[i] is the count of '1' in S[:i]
        zeros = [0]*(n+1)   # zeros[i] is the count of '0' in S[-i:]
        for i in range(1, n+1):
            ones[i] = ones[i-1] + 1 if S[i-1] == '1' else ones[i-1]
            zeros[i] = zeros[i-1] + 1 if S[-i] == '0' else zeros[i-1]
        
        ans = 20001
        for i in range(n+1):
            ans = min(ans, ones[i] + zeros[n-i])
        
        return ans

test_cases = ['0', '1', '01', '10', '00', '11', '00110', '010110', '000110', '101010', "00011000"]
for S in test_cases:
    print(S, end = ' -> ')
    print(Solution().minFlipsMonoIncr(S))        