"""
953 Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
"""
import unittest
from itertools import zip_longest
class Solution:
    # my own solution, decode the alien word to normal alphabet word
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        mirror = {a:chr(i + ord('a')) for i, a in enumerate(order)}

        for i in range(len(words) - 1):
            length = min(len(words[i]), len(words[i+1]))
            for j in range(length):
                c1, c2 = mirror[words[i][j]], mirror[words[i+1][j]]
                if c1 > c2:
                    return False
                elif c1 < c2:
                    break
            else:
                if len(words[i]) > len(words[i+1]):
                    return False
        
        return True
    
    # 2nd visit on 7/20/2020, using zip_longest to align two words
    def isAlienSorted2(self, words, order):
        length = len(words)
        if length < 2: return True
        pos = {char:i for i, char in enumerate(order)}
        pos[''] = -1 # '' is always smaller than others
        for i in range(length-1):
            word1, word2 = words[i], words[i+1]
            for c1, c2 in zip_longest(word1, word2, fillvalue=''):
                if c1 == c2:
                    continue
                elif pos[c1] < pos[c2]:
                    break
                else:
                    return False
                
        return True

class Test(unittest.TestCase):
    def test_empty(self):
        test = Solution()
        self.assertTrue(test.isAlienSorted2([], "a"))

    def test_1(self):
        test = Solution()
        self.assertFalse(test.isAlienSorted2(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))

    def test_2(self):
        test = Solution()
        self.assertFalse(test.isAlienSorted2(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))

if __name__ == "__main__":
    unittest.main(exit = False)

