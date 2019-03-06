"""
Missing Words

Given two sentences, s and t, t is a subsequence of s if all of the words in t occur in thesame order within s. 
Words do not have to appear contiguously in s, but order must bemaintained. 
For example, given the sentence “I like cheese”, one example of a subsequence would be “I cheese”.

You will be given two sentences, s and t. It is guaranteed that string t isa subsequence of string s. 
When reading string s from left to right, locate the firstoccurrence of subsequence t. 
Remove this subsequence and return the remainingelements of string s in order.

Example:
s = I like eating cheese do you like cheese
t = like cheese
Return: I eating do you like cheese

Constraints:
1. Strings s and t consist of English alphabetic letters (i.e., a−z and A−Z) and spacesonly.
2. 1 ≤ |t| ≤ |s| ≤ 10^6
3. 1 ≤ length of any word in s or t ≤ 15
4. It is guaranteed that string t is a subsequence of string s.
"""
class Solution:
    def missingWords(self, s, t):
        """
        s, t: space separated words
        return a list of missing words
        """
        s_words, t_words = s.split(), t.split()
        i, j, res = 0, 0, []
        for i in range(len(s_words)):
            if j < len(t_words) and s_words[i] == t_words[j]:
                j += 1
            else:
                res.append(s_words[i])

        return res

s = "I like eating cheese do you like cheese"
t = "like cheese"
print(Solution().missingWords(s, t))