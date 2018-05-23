"""

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
class Solution:
    # use 26 bits to represent if each s's letter's count is the same as p
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        count_s, count_p, base = [0]*26, [0]*26, ord('a')
        expected = 0
        for c in p:
            index = ord(c) - base
            count_p[index] += 1
            expected |= 1 << index  # bug fixed: initially set all 26 bits to 1, we should leave the unused letter's bit as 0
        
        i, encode = 0, 0
        res = []
        for j, c in enumerate(s):
            index = ord(c) - base
            count_s[index] += 1
            if count_s[index] == count_p[index]:
                encode |= 1<<index
            else:
                encode &= expected - (1<<index)
            #if encode == expected:
            #    res.append(i)
            if j - i + 1 == len(p):
                if encode == expected:
                    res.append(i)
                    
                index = ord(s[i]) - base
                count_s[index] -= 1
                # bug fixed: forgot to update the encode
                if count_s[index] == count_p[index]:
                    encode |= 1<<index
                else:
                    encode &= expected - (1<<index)

                i += 1
        
        return res

s= "baa"
p= "aa"
obj = Solution()
print(obj.findAnagrams(s, p))