"""
399 Evaluate Division

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). 
Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
from collections import deque
class Solution:
    # my own solution, using graph and BFS
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # put a -> b, b -> a and their values (a/b, b/a) into graph
        graph = {}
        for i, vars in enumerate(equations):
            a, b = vars[0], vars[1]
            if a == b:
                continue
            # add {a: {b: value}}
            if a not in graph:
                graph[a] = {}                
            graph[a][b] = values[i]
            # add {b: {a: 1.0/value}}
            if abs(values[i]) > 1e-10:  # we must exclude 1.0/0.0
                if b not in graph:
                    graph[b] = {}
                graph[b][a] = 1.0/values[i]

        res = []
        for query in queries:
            a, b = query[0], query[1]
            if a not in graph or b not in graph:
                res.append(-1.0)
                continue
            if a == b:
                res.append(1.0)
                continue

            # BFS to get the answer
            q = deque()
            q.append((a, 1.0))  # initially put tuple (variable, value) into queue
            visited = set()
            #visited.add(a) # bug fixed: should not add "a" into visited set, otherwise it won't pass the check below
            while len(q) > 0:
                src, val = q.popleft()
                # check visited property
                if src in visited:
                    continue
                else:
                    visited.add(src)
                # a/b is found, just return
                if src == b:
                    res.append(val)
                    break
                # push corresponding denominators into queue
                denoms = graph[src]
                for (k, v) in denoms.items():
                    q.append((k, v*val))
            else:   # bug fixed: forgot to use else
                res.append(-1.0)

        return res

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
obj = Solution()
print(obj.calcEquation(equations, values, queries))

# 弗洛伊德算法 http://www.cnblogs.com/grandyang/p/5880133.html   ?
#         