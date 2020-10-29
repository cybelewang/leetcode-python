"""
527 Word Abbreviation

Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, 
a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. 
In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.
"""
class Solution:
    # https://www.cnblogs.com/grandyang/p/6818742.html
    # for each words[i], iterate all words[j] after it and keep increasing prefix length until no words[j] has conflict with words[i]
    # therefore we need a preLen list which tracks the prefix length of each word
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        # get abbreviate of word with prefix length
        def abbreviate(word, prefixLength):
            if len(word) - prefixLength <= 2:
                return word
            else:
                return word[:prefixLength] + str(len(word)-prefixLength-1) + word[-1:]
        
        n = len(dict)
        preLen = [1]*n
        res = [abbreviate(word, 1) for word in dict]
        for i in range(n):
            while True:
                conflict = set()
                for j in range(i+1, n):
                    if res[j] == res[i]:
                        conflict.add(j)
                if not conflict:
                    break
                conflict.add(i)
                for idx in conflict:
                    preLen[idx] += 1
                    res[idx] = abbreviate(dict[idx], preLen[idx])
        return res