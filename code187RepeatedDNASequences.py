"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        count, res = {}, []
        for i in range(0, len(s)-9):
            sub = s[i:i+10]
            if sub in count:
                count[sub] += 1
                if count[sub] == 2:
                    res.append(sub)
            else:
                count[sub] = 1
        
        return res

test_str = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
obj = Solution()
print(obj.findRepeatedDnaSequences(test_str))