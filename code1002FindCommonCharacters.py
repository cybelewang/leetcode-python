"""
1002 Find Common Characters

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""
from collections import Counter
class Solution:
    def commonChars(self, A):
        """
        :type A: list[str]
        :rtype: list[str]
        """
        min_repeat = [100]*26
        for s in A:
            count = Counter(s)
            for i in range(26):
                min_repeat[i] = min(min_repeat[i], count[chr(i + ord('a'))])
        
        letters = []
        for i in range(26):
            repeat = min_repeat[i]
            letter = chr(i + ord('a'))
            letters.extend([letter]*repeat)

        return letters

#A = ["bella","label","roller"]
A = ["a"]
print(Solution().commonChars(A))