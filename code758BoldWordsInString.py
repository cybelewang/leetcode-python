"""
758 Bold Words in String

Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Note:

words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.
"""
# similar problems: 45 Jump Game II
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/8531642.html
    # originally thought the method of extending the bold end, similar to problem 45 Jump Game II
    # originally I was thinking how to generate the "res" when iterating the S, but figured out it was hard to update the bold start index without the help of a bold array
    def boldWords(self, words, S):
        n = len(S)
        res, end = '', 0    # end is the current ending index to be bold
        bold = [False]*n    # bold[i] indicates if S[i] is bold
        for i in range(n):
            for word in words:
                m = len(word)
                if i + m <=n and S[i:i+m] == word:
                    end = max(end, i+m)
            bold[i] = end > i
        
        i = 0
        while i < n:
            if not bold[i]:
                res += S[i]
                i += 1
                continue
            res += "<b>"
            j = i
            while j < n and bold[j]:
                j += 1
            res += S[i:j] + "</b>"
            i = j
        
        return res
    
words = ["ab", "bc"]
S = "aabcd"
print(Solution().boldWords(words, S))