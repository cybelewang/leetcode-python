"""
30 Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. 
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

"""
First of all consider s as several series of words with length k starting at [0, k-1]. For example "barfoothe" with k = 3, can be view as ["bar", "foo", "the"] for i=0 and ["arf", "oot"] for i = 1 and ["rfo", "oth"] for i = 2.
Thus we need to check each of these series and find out the valid index by definition.

For each series, we just need to check if there exist a range [l, r) where the occurrence or "spectrum" of the words in the range is the same as our given word list's "spectrum". We use dictionary to store the spectrum and maintain it as we loop through s.

collections.Counter class may save a bit of code on updating the counts of the dictionary. However plain dict wins on the speed.
"""
import unittest
from collections import Counter
def _findSubstring(l, r, n, k, t, s, req, ans):
    curr = {}
    while r + k <= n:
        w = s[r:r + k]
        r += k
        if w not in req:
            l = r
            curr.clear()
        else:
            curr[w] = curr[w] + 1 if w in curr else 1
            while curr[w] > req[w]:
                curr[s[l:l + k]] -= 1
                l += k
            if r - l == t:
                ans.append(l)

def findSubstring(s, words):
    if not s or not words or not words[0]:
        return []
    n = len(s)
    k = len(words[0])
    t = len(words) * k
    req = {}
    for w in words:
        req[w] = req[w] + 1 if w in req else 1
    ans = []
    for i in range(min(k, n - t + 1)):
        _findSubstring(i, i, n, k, t, s, req, ans)
    return ans

def findSubstring3(s, words):
    if not s or not words or not words[0]:
        return []
    n = len(s)
    k = len(words[0])
    t = len(words) * k
    req = {}
    for w in words:
        req[w] = req[w] + 1 if w in req else 1
    ans = []
    for i in range(min(k, n - t + 1)):
        findSubstring4(i, n, k, t, s, req, ans)
    return ans

def findSubstring4(l, n , k, t, s, req, ans):
    curr = {}

    for i in range(l, l + t, k):
        substr = s[i : i+k]
        if substr in req:
            curr[substr] = curr[substr] + 1 if substr in curr else 1
    
    if curr == req:
        ans.append(l)

    left = s[l : l+k]
    l += k
    r = l + t
    while r <= n:        
        right = s[r-k : r]
        if left in curr:
            curr[left] = curr[left] - 1 if curr[left] > 0 else 0
        if right in req:
            curr[right] = curr[right] + 1 if right in curr else 1
        if curr == req:
            ans.append(l)
        left = s[l : l+k]
        l += k
        r = l + t

# revisited on 1/10/2020
def findSubstring2(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if not s or not words:
        return []

    count, res = Counter(words), []
    m = len(words[0])
    n = m*len(words)
    for i in range(len(s) - n + 1):
        subCnt = Counter()
        for j in range(i, i + n, m):
            ss = s[j:j+m]
            subCnt[ss] += 1
            if subCnt[ss] > count[ss]: # handle two cases: (1) ss exist in words but subCnt[ss] > count[ss] (2) ss doesn't exist, so 1 > (count[ss] = 0)
                break
        else:
            res.append(i)
    
    return res

class Test(unittest.TestCase):
    def test_1(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","good"]
        self.assertEqual(findSubstring2(s, words), [8])

if __name__ == "__main__":
    unittest.main(exit = False)
