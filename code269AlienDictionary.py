"""
269 Alien Dictionary    -   not submitted

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""
from collections import defaultdict, deque
class Solution:
    # my own solution using lexicorgraphical comparison and topological order
    def alienOrder(self, words):
        """
        :type words: list[str]
        :rtype: str
        """
        # step 1: construct graph and in-degree dict 
        graph = defaultdict(list)
        indegrees = {}
        for w in words:
            for c in w:
                indegrees.setdefault(c, 0)

        for i in range(1, len(words)):
            pre, post = words[i-1], words[i]
            for j in range(min(len(pre), len(post))):
                if pre[j] != post[j]:
                    # pre[j] must be smaller than post[j] in alien dictionary
                    graph[pre[j]].append(post[j])   # create an edge in graph
                    indegrees[post[j]] += 1 # increase the in-degree of post[j]
                    break   # no need to check remaining characters in pre and post
        
        # step 2: topological sort using BFS and in-degree method
        order = []
        q = deque(a for a in indegrees if indegrees[a] == 0)
        while q:
            a = q.popleft()
            order.append(a)
            for b in graph[a]:
                indegrees[b] -= 1
                if indegrees[b] == 0:
                    q.append(b)
        
        if any(x for x in indegrees if indegrees[x] != 0):
            return ''
        else:
            return ''.join(order)

words = [] # expect ''
words = ['z', 'x', 'z'] # expect ''
words = ['a', 'ac', 'acb']  # expect any order of 'abc'
words = ["wrt", "wrf", "er", "ett", "rftt"] # expect 'wertf'
print(Solution().alienOrder(words))