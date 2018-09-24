"""
472 Concatenated Words


Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""
# similar problems: 139, 140
# use problem 139's solution
# http://www.cnblogs.com/grandyang/p/6254527.html
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        wordDict = set(words)
        res = []

        for word in wordDict:
            #wordDict.remove(word)
            n = len(word)
            if n == 0: continue # bug fixed: '' should not be in the result
            dp = [False]*(n + 1)
            dp[0] = True
            for j in range(1, n + 1):
                for i in range(0, j):
                    if j-i < n and dp[i] and word[i:j] in wordDict:
                        dp[j] = True
                        break
            if dp[n]:
                res.append(word)

            #wordDict.add(word)

        return res

words = [""]
#words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
obj = Solution()
print(obj.findAllConcatenatedWordsInADict(words))