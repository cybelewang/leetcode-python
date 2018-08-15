"""
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""
# similar problems: 161 One Edit Distance
from collections import defaultdict
# a solution using one edit distance
# another solution is to convert dict list to a set, then change every character of word from 'a' to 'z' but skp itself, then check if the new word is in the set
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = defaultdict(list)   # key: length, value: list of same length words

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.mem[len(word)].append(word)        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        # check word with every word in the same length list and see if they are one edit distance
        n = len(word)
        for w in self.mem[n]:
            cnt = 0
            for i in range(n):
                if w[i] != word[i]:
                    cnt += 1

            if cnt == 1:
                return True

        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)