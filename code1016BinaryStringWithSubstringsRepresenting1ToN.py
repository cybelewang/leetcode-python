"""
1016. Binary String With Substrings Representing 1 To N
Medium

26

122

Favorite

Share
Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

 

Example 1:

Input: S = "0110", N = 3
Output: true
Example 2:

Input: S = "0110", N = 4
Output: false
 

Note:

1 <= S.length <= 1000
1 <= N <= 10^9
"""
class Solution:
    def queryString(self, S: str, N: int) -> bool: