"""
884 Uncommon Words from Two Sentences

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""
from collections import Counter
class Solution:
    # understand the problem correctly: appears exactly once, so remove those appear more than once
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        cntA, cntB = Counter(A.split()), Counter(B.split())
        res = []
        for a in cntA:
            if cntA[a] == 1 and cntB[a] == 0:
                res.append(a)
        
        for b in cntB:
            if cntB[b] == 1 and cntA[b] == 0:
                res.append(b)

        return res

        # failed on A = "s z z z s", B = "s z ejt", expected ["ejt"]
        # def G(S):
        #     # generator to yield word that appears only once in string S
        #     count = Counter(S.split())
        #     for word in count:
        #         if count[word] == 1:
        #             yield word
        
        # return list(set(G(A)) ^ set(G(B)))
        
        # original wrong solution
        #return list(set(A.split()) ^ set(B.split()))

#A = "this apple is sweet"
#B = "this apple is sour"

A = "s z z z s"
B = "s z ejt"
print(Solution().uncommonFromSentences(A, B))

"""
Input
"apple apple"
"banana"
Output
["apple","banana"]
Expected
["banana"]
"""