"""
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


# TLE solution
def findSubstring2(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    result = []

    if len(words) == 0:
        return result

    standard = {}
    for word in words:
        if word in standard:
            oldValue = standard[word]
            standard[word] = oldValue + 1
        else:
            standard[word] = 1
    m = len(words[0])
    l = m*len(words)
    for i in range(len(s) - l + 1):
        my_dict = {}
        for j in range(i, i + l, m):
            sub = s[j:j+m]
            if sub in my_dict:
                oldValue = my_dict[sub]
                my_dict[sub] = oldValue + 1
            else:
                my_dict[sub] = 1
        if my_dict == standard:
            result.append(i)
    
    return result

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]            
print(findSubstring(s, words))
