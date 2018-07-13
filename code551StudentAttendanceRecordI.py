"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""
from collections import Counter
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # ask about empty string
        count = Counter(s)
        return (count['A'] < 2) and (count['L'] < 3)    # beauty of collections.Counter: if the key doesn't exist in Counter, it just return 0 instead of inserting records, or raising exceptions

test_cases = ['', 'PPALLP', 'PPALLL']
for s in test_cases:
    print(Solution().checkRecord(s))