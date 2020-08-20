"""
1087 Brace Expansion

A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order. 

Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: "abcd"
Output: ["abcd"]

Note:

1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.
"""
import itertools
class Solution:
    # since option letters are unique, we can use itertools.product to generate all of them
    # https://leetcode.com/problems/brace-expansion/discuss/314308/Python-3-line-Using-Product
    def expand(self, S: str) -> List[str]:
        A = S.replace('{', ' ').replace('}', ' ').strip().split(' ')
        B = [sorted(a.split(',')) for a in A]
        return [''.join(c) for c in itertools.product(*B)] 
   
    # use itertools.groupby, note that k and grp shares iterator, so when k advances, grp will change too.
    # pitfall when merging letters in lexicographical order: for example, when we have ['a', 'a'] and ['b', 'c'], both are sorted.
    # If we merge them using two for loops, we will get ['ab', 'ac', 'ab', 'ac'], not in lexicographical order
    # We need to repeat 'ab' when 'a' has duplicates, but actually this problem says all letters in curly brackets are different.
    def expand(self, S: str) -> List[str]:
        n, i = len(S), S.find('{')
        if i == -1: return [S]        
        j = S.find('}', i+1)
            
        options = sorted(S[i+1:j].split(','))
        remains = self.expand(S[j+1:])
        res = []
        for k, grp in itertools.groupby(options):
            duplicate = len(list(grp)) # need to store grp info first before iterator advances
            for right in remains:
                res.extend([S[:i] + k + right]*duplicate)
        return res