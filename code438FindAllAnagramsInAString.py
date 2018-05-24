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
        def updateBits(index, increment, count_s, count_p, encode):
            """
            update encode by adding or removing alphabet[index] from the window
            index: the letter index in alphabet
            increment: the increment count of alphabet[index], either 1(add) or -1(remove)
            return updated encode
            """
            count_s[index] += increment
            if count_s[index] == count_p[index]:
                encode |= 1 << index
            else:
                encode &= (1<<26) - 1 - (1<<index)
            
            return encode
            
        count_s, count_p, base = [0]*26, [0]*26, ord('a')
        expected = (1<<26) - 1  # this is expected encode int, with all 26 bits set to 1
        encode = expected
        # count each letter in p
        # reset the bit with corresponding letter's count > 0
        # the bit of the letters not in p will remain 1
        for c in p:
            index = ord(c) - base
            count_p[index] += 1
            encode &= (1<<26) - 1 - (1<<index)
        
        # now encode is sitting in initial value, with 0 means count not matching, and 1 means count matching
        i = 0   # start index of the fixed-size window
        res = []
        for j in range(len(s)):
            # add j into window
            encode = updateBits(ord(s[j])-base, 1, count_s, count_p, encode)
            if j - i + 1 == len(p):
                if encode == expected:
                    res.append(i)
                # remove s[i] from window
                encode = updateBits(ord(s[i])-base, -1, count_s, count_p, encode)
                i += 1
                
        return res

s= "cbaebabacd"
p= "abc"
obj = Solution()
print(obj.findAnagrams(s, p))