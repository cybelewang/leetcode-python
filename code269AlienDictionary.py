"""
269 Alien Dictionary

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
import unittest
from collections import defaultdict, deque
class Solution:
    # my own solution using lexicorgraphical comparison and topological order
    def alienOrder_BFS(self, words):
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
            else:
                if len(pre) > len(post): return '' # invalid because first is larger than second
        
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

    def alienOrder_DFS(self, words):
        # Recursive helper function to create the topological sorted letters
        def helper(src, graph, colors, res):
            # return False if there is a cycle
            if colors[src] == 2: return True
            if colors[src] == 1: return False
            colors[src] = 1 # visiting src now
            for dst in graph[src]:
                if not helper(dst, graph, colors, res):
                    return False
            colors[src] = 2 # completed visiting
            res.append(src)
            return True

        # create graph
        colors, graph = {}, defaultdict(set)
        for i in range(1, len(words)):
            first, second = words[i-1], words[i]
            for j in range(min(len(first), len(second))):
                a, b = first[j], second[j]
                if a != b:
                    graph[a].add(b) # create an edge in graph a -> b
                    break
            else:
                if len(first) > len(second): return '' # invalid because first is longer than second

        # initialize colors of all letters
        for word in words:
            for a in word:
                colors[a] = 0
        
        res = []
        for node in colors:
            if not helper(node, graph, colors, res):
                return ''
        
        return ''.join(res[::-1])

obj = Solution()
class Test(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(obj.alienOrder_BFS([]), '')
        self.assertEqual(obj.alienOrder_DFS([]), '')
    
    def test_invalid(self):
        self.assertEqual(obj.alienOrder_BFS(['z', 'x', 'z']), '')
        self.assertEqual(obj.alienOrder_DFS(['z', 'x', 'z']), '')

    def test_smallsets(self):
        self.assertEqual(sorted(obj.alienOrder_BFS(['a', 'ac', 'acb'])), sorted('acb')) # expect any order of "abc"
        self.assertEqual(obj.alienOrder_BFS(["wrt", "wrf", "er", "ett", "rftt"]), 'wertf')
        self.assertEqual(sorted(obj.alienOrder_DFS(['a', 'ac', 'acb'])), sorted('acb')) # expect any order of "abc"
        self.assertEqual(obj.alienOrder_DFS(["wrt", "wrf", "er", "ett", "rftt"]), 'wertf')

    def test_invalidWords(self):
        self.assertEqual(obj.alienOrder_BFS(["abc", "ab"]), "")
        self.assertEqual(obj.alienOrder_DFS(["abc", "ab"]), "")

if __name__ == '__main__':
    unittest.main(exit = False)