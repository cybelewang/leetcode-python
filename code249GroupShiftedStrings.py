"""
249 Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""
# similar to 49 Group Anagrams
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def encode(s):
            if s == '':
                return '#'
            a = ['0']
            for i in range(1, len(s)):
                diff = (ord(s[i])-ord(s[0]) +26)%26
                a.append(str(diff))
            return '#'.join(a)
        
        mem, res = {}, []
        for s in strings:
            es = encode(s)
            if es in mem:
                res[mem[es]].append(s)
            else:
                mem[es] = len(res)
                res.append([s])
        
        return res