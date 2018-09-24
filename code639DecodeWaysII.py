"""
639 Decode Ways II

A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 10^9 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 10^5].
The input string will only contain the character '*' and digits '0' - '9'.
"""
# similar problems: 91 Decode Ways
class Solution:
    # my own solution using a dict
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        M = 10**9 + 7
        n = len(s)
        dp = [0]*(n+1)  # dp[i] is the number of decode ways for string with length i

        # create a lookup table
        table = {str(num):1 for num in range(1,27)} # for 1 to 26, they only have 1 way
        table['*'] = 9  # '1' to '9'
        table['1*'] = 9    # '11' to '19'
        table['2*'] = 6     # '21' to '26'
        table['**'] = 15    # table['1*'] + table['2*']

        # '*0' to '*6'
        for num in range(7):
            table['*'+str(num)] = 2 # * can be 1 or 2, for example, when num = 6, it could be 16 or 26
        # '*7' to '*9'
        for num in range(7,10):
            table['*'+str(num)] = 1 # * can only be 1 if num > 6

        # DP
        dp[0], dp[1] = 1, table.get(s[0], 0)        
        for i in range(2, n+1):
            # single letter s[i-1]
            dp[i] = (table.get(s[i-1], 0) * dp[i-1])%M
            # two letters s[i-2:i]
            dp[i] = (dp[i] + table.get(s[i-2:i], 0) * dp[i-2])%M

        return dp[n]

test_cases = ['0', '1', '*', '012', '**', '1*', '2*', '***']      
obj = Solution()
for s in test_cases:
    print(s, end = ' -> ')
    print(obj.numDecodings(s))      