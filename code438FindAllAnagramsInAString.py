"""
438 Find All Anagrams in a String

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
# similar problems: 567
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
        # reset the bit to 0 for p lettes with count > 0
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

# 7/25/2020
# Use 26 bits to represent the match condition, but we use compare like "match & base == base" to filter out those letters not in p. Bit 1 in base represents that letter is in p.
# We only need to compare s letters which are also in p, and ignore other letters, because the length of substring is fixed. If there are other s letters not in p, then some letters in p must not match the count.
class Solution2:
    def findAnagrams(self, s, p):
        self.sCnt = defaultdict(int)
        self.pCnt = Counter(p) # bug fixed: forgot to declare members
        self.match = 0
        base = 0 # bit mask of p anagrams
        res = []
        for letter in self.pCnt:
            base |= 1 << (ord(letter) - ord('a'))
        for i in range(len(s)):
            self.addLetter(s[i])
            if i < len(p)-1: continue # bug fixed: must consider i == len(p) - 1 and i == len(p) differently
            # need to evaluate self.match when i >= len(p) -1, not i >= len(p)
            if i >= len(p):
                self.removeLetter(s[i-len(p)])
            if self.match & base == base:
                res.append(i-len(p)+1)
        return res
    
    # add a character to a window and update match bits
    def addLetter(self, letter):
        self.sCnt[letter] += 1
        self.updateMatch(letter)
    
    # remove a character to a window and update match bits
    def removeLetter(self, letter):
        self.sCnt[letter] -= 1
        self.updateMatch(letter)
    
    # helper function to update match bits
    def updateMatch(self, letter):
        if self.sCnt[letter] == self.pCnt[letter]:
            self.match |= 1 << (ord(letter) - ord('a'))
        else:
            self.match &= ~(1 << (ord(letter) - ord('a')))

    from collections import Counter
    def findAnagrams2(self, s: str, p: str):
        m, n = len(p), len(s)
        count, req = Counter(p), m
        res = []
        for j, c in enumerate(s):
            if c in count:
                count[c] -= 1
                if count[c] >= 0:
                    req -= 1
            if j + 1 > m:
                i = j - m
                if s[i] in count:
                    count[s[i]] += 1
                    if count[s[i]] > 0:
                        req += 1
            if j >= m - 1:
                if req == 0:
                    res.append(j - m + 1)
        return res

s= "cbaebabacd"
p= "abc"
obj = Solution()
print(obj.findAnagrams(s, p))